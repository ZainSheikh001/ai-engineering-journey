from pydantic import BaseModel, ValidationError


class CiteAnswer(BaseModel):
    answer: str
    citations: list[str]
    is_answerable: bool


def check_answer(raw):
    """Check one LLM answer. Return a verdict as text."""
    try:
        result = CiteAnswer.model_validate_json(raw)
    except ValidationError:
        return "Invalid: wrong shape"

    if result.is_answerable == False and len(result.citations) > 0:
        return "Invalid: fake citation"

    return "Valid"


good = '{"answer": "Minimum age is 18.", "citations": ["Section 1.1"], "is_answerable": true}'
bad = '{"answer": "Minimum age is 18.", "citations": "Section 1.1", "is_answerable": true}'
fake_section = '{"answer": "Minimum age is 18.", "citations": ["Section 9.4"], "is_answerable": true}'
print("fake_section:", check_answer(fake_section))
print("good:", check_answer(good))
print("bad:", check_answer(bad))
