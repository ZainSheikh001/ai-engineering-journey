from answer_guard import check_answer


def test_good_answer_is_valid():
    raw = '{"answer": "Minimum age is 18.", "citations": ["Section 1.1"], "is_answerable": true}'
    assert check_answer(raw) == "Valid"


def test_wrong_shape_is_rejected():
    raw = '{"answer": "Minimum age is 18.", "citations": "Section 1.1", "is_answerable": true}'
    assert check_answer(raw) == "Invalid: wrong shape"


def test_citation_when_unsure_is_rejected():
    raw = '{"answer": "I am not sure.", "citations": ["Section 1.1"], "is_answerable": false}'
    assert check_answer(raw) == "Invalid: fake citation"


def test_nonexistent_section_is_rejected():
    raw = '{"answer": "Minimum age is 18.", "citations": ["Section 9.4"], "is_answerable": true}'
    assert check_answer(raw) == "Invalid: section does not exist"