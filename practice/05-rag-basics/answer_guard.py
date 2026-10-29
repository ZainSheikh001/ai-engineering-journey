from pydantic import BaseModel, ValidationError

VALID_SECTIONS = ["Section 1.1", "Section 1.2", "Section 2.1", "Section 2.2", "Section 3.1", "Section 3.2"]


class CiteAnswer(BaseModel):
    answer: str
    citations: list[str]
    is_answerable: bool


def check_answer(raw):
    """Check one LLM answer. Return a verdict as text."""
    # Check 1: right types?
    try:
        result = CiteAnswer.model_validate_json(raw)
    except ValidationError:
        return "Invalid: wrong shape"

    # Check 2: unsure but still citing?
    if result.is_answerable == False and len(result.citations) > 0:
        return "Invalid: fake citation"

    # Check 3: does every cited section really exist?
    for c in result.citations:
        if c not in VALID_SECTIONS:
            return "Invalid: section does not exist"

    return "Valid"