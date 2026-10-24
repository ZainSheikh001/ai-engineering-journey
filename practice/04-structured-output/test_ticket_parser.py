from ticket_parser import parse_ticket

def test_valid_ticket_is_accepted():
    raw_text = '{"category": "refund", "urgency": "high", "needs_human": true}'
    ticket = parse_ticket(raw_text)
    assert ticket is not None
    assert ticket.category == "refund"

def test_invalid_ticket_is_rejected():
    raw_text = '{"category": "refund"}'
    ticket = parse_ticket(raw_text)
    assert ticket is None

def test_invalid_urgency_is_rejected():
    raw_text = '{"category": "refund", "urgency": "urgent", "needs_human": true}'
    ticket = parse_ticket(raw_text)
    assert ticket is None