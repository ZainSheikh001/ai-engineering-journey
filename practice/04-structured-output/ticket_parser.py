from typing import Literal
from pydantic import BaseModel, ValidationError

class Ticket(BaseModel):
    category: Literal["order", "refund", "complaint", "other"]
    urgency: Literal["low", "medium","high"]
    needs_human: bool

def  parse_ticket(raw_text):
    """Turn LLM text into a Ticket. Return None if the text is invalid."""
    try: 
        return Ticket.model_validate_json(raw_text)
    except ValidationError as e:
        print("INVALID OUTPUT - would retry or send to a human")
        print(e)
        return None