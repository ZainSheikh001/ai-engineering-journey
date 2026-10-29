from dotenv import load_dotenv 
from pydantic import BaseModel, ValidationError
from groq import Groq

load_dotenv()
client = Groq()
MODEL = "openai/gpt-oss-20b"

DOCUMENT = """
Practice document (fictional): Example Microfinance Bank - Account Opening Policy 2026

Section 1. Eligibility
1.1 Applicants must be at least 18 years old.
1.2 Applicants must hold a valid CNIC.

Section 2. Required documents
2.1 A copy of the CNIC.
2.2 Proof of address, such as a recent utility bill.

Section 3. Account types
3.1 Basic Banking Account: no minimum balance.
3.2 Business Account: minimum balance of PKR 25,000.
"""

RULES = (
"You are a compliance assistant. "
    "Answer ONLY using the document provided by the user. "
    "Reply in JSON with exactly three keys: answer, citations, is_answerable. "
    "answer is text. "
    "citations is a list of section names, for example Section 1.1 and Section 3.2. "
    "is_answerable is true or false. "
    "If the answer is not in the document: answer is I am not sure., citations is an empty list, is_answerable is false. "
    "When you do answer, put EVERY section you used in citations."
)

class CiteAnswer(BaseModel):
    answer: str
    citations: list[str]
    is_answerable: bool

# ---------- INSPECTOR (from Drill 7) ----------

def check_answer(raw):
        """Check one LLM answer. Return a verdict as text."""
        try:
              result = CiteAnswer.model_validate_json(raw)

        except ValidationError:
                return "Invalid: wrong shape"
        if result.is_answerable == False and len(result.citations) > 0:
                return "Invalid: fake citation"
        return "Valid"

# ---------- PRODUCER (from Drill 6, now JSON) ----------
def ask_json(question):
    """Send the document plus a question to the LLM and return its raw JSON text."""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": RULES},
            {"role": "user", "content": f"DOCUMENT:\n{DOCUMENT}\n\nQUESTION: {question}"},
        ],
        response_format={"type": "json_object"},
    )
    return response.choices[0].message.content

# ---------- PIPELINE: producer -> inspector ----------

questions = [
    "What is the minimum age to open an account?",
    "What is the interest rate on savings accounts?",
    "Can a 17-year-old open a Business Account if they have PKR 30,000?",
]

for q in questions:
    raw = ask_json(q)
    print("QUESTION:", q)
    print("RAW:", raw)
    print("VERDICT:", check_answer(raw))
    print("-" * 40)