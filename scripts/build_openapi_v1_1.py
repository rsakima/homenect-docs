from pathlib import Path

BASE = Path('07_system/openapi/HOMENECT_OpenAPI_v1.0.yaml')
OUT = Path('07_system/openapi/HOMENECT_OpenAPI_v1.1.yaml')

lines = BASE.read_text(encoding='utf-8').splitlines()
out = []
current_path = None
current_schema = None
in_reservation_post = False

for i, line in enumerate(lines):
    stripped = line.strip()
    indent = len(line) - len(line.lstrip(' '))

    # Track path and operation.
    if indent == 2 and stripped.startswith('/') and stripped.endswith(':'):
        current_path = stripped[:-1]
        in_reservation_post = False
    elif indent == 4 and stripped == 'post:':
        in_reservation_post = current_path == '/reservations'
    elif indent == 4 and stripped in {'get:', 'put:', 'patch:', 'delete:'}:
        in_reservation_post = False

    # Track component schema names.
    if indent == 4 and stripped.endswith(':') and not stripped.startswith(('/', 'get:', 'post:', 'put:', 'patch:', 'delete:')):
        name = stripped[:-1]
        if name in {
            'Error','Money','ReservationStatus','HandoffType','ReservationSummary',
            'CreateReservationRequest','AvailabilityResult','JobOffer','HelpRequest',
            'Referral','AdditionalWork','WorkLogRequest','CashReceiptRequest',
            'IncidentRequest','TransitionRequest','SubsidyApprovalRequest'
        }:
            current_schema = name

    # Version bump only in info.version.
    if line == '  version: 1.0.0':
        out.append('  version: 1.1.0')
        continue

    # Reservation creation now requires bearer auth; remove its local public override.
    if in_reservation_post and indent == 6 and stripped == 'security: []':
        continue

    # ReservationSummary: customer_price_locked is not required until CONFIRMED.
    if current_schema == 'ReservationSummary' and indent == 6 and stripped == '- customer_price_locked':
        continue

    # ReservationSummary: allow null before CONFIRMED.
    if current_schema == 'ReservationSummary' and indent == 8 and stripped == 'customer_price_locked:':
        out.extend([
            line,
            '          oneOf:',
            "          - $ref: '#/components/schemas/Money'",
            "          - type: 'null'",
            '          description: REQUESTED / MATCHINGではnull可。CONFIRMED以降はBusiness Ruleで必須。',
        ])
        # Skip the immediately following old $ref line.
        if i + 1 < len(lines) and lines[i + 1].strip().startswith('$ref:'):
            lines[i + 1] = '__SKIP_OLD_PRICE_REF__'
        continue

    if stripped == '__SKIP_OLD_PRICE_REF__':
        continue

    # Normal JobOffer compensation is distinct from HELP support_payout.
    if current_schema == 'JobOffer':
        if indent == 6 and stripped == '- support_payout':
            out.append('      - partner_compensation')
            continue
        if indent == 8 and stripped == 'support_payout:':
            out.append('        partner_compensation:')
            continue

    out.append(line)

text = '\n'.join(out).rstrip() + '\n'

checks = [
    'version: 1.1.0',
    'partner_compensation:',
    'REQUESTED / MATCHINGではnull可',
]
for token in checks:
    if token not in text:
        raise SystemExit(f'missing generated token: {token}')

# The reservation POST must no longer be locally public.
reservation_block = text.split('  /reservations:\n', 1)[1].split('\n  /reservations/{id}:', 1)[0]
if 'security: []' in reservation_block:
    raise SystemExit('reservation POST is still public')

OUT.write_text(text, encoding='utf-8')
print(f'generated {OUT}')
