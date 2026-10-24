from dbm import error

from pydantic import BaseModel, ValidationError

class Ticket (BaseModel):
    category: str 
    urgency: str
    needs_human: bool

llm_text = '{"category": "refund", "urgency": "high", "needs_human": "True"}'
try:
    ticket = Ticket.model_validate_json(llm_text)    
    print("validation done" , ticket)

except ValidationError as e:
        print("The LLM's data failed the checklist.")
        print(e)
