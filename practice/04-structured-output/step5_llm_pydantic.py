from typing import Literal
from dotenv import load_dotenv
from groq import  Groq 
from pydantic import BaseModel, ValidationError
load_dotenv()
client = Groq()

MODEL = "openai/gpt-oss-20b"

RULES = ("You classify customer support messages for a Pakistani online shop. "
    "Messages may be in English or Roman Urdu. "
    "Reply ONLY with a json object (JSON) with exactly these keys: "
    '"category" (one of: "order", "refund", "complaint", "other"), '
    '"urgency" (one of: "low", "medium", "high"), '
    '"needs_human" (true or false).'
)

CUSTOMER_MESSAGE = "Mera order 10 din se nahi aya, paise wapas chahiye abhi!"

class Ticket(BaseModel):
    category: Literal["order", "refund", "complaint", "other"]
    urgency: Literal["low", "medium", "high"]
    needs_human: bool

response = client.chat.completions.create(
    model=MODEL,
    messages= [
        {"role" : "system", "content" : RULES},
        {"role" :"user", "content" : CUSTOMER_MESSAGE}
    ],
    response_format={"type": "json_object"},

)


raw_text = response.choices[0].message.content
print("Raw text from the LLM:\n", raw_text)

try:
    ticket = Ticket.model_validate_json(raw_text)
    print("Validation done. Ticket:", ticket)
    print("Category:", ticket.category)
    print("Need Human?", ticket.needs_human)
except ValidationError as e:
    print("INVALID OUTPUT - would retry or send to a human")
    print(e)