from dotenv import load_dotenv
from groq import Groq
load_dotenv()
client = Groq()
MODEL = "openai/gpt-oss-20b"
DOCUMENT ="""
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
    "If the answer is not in the document, reply exactly: I am not sure. "
    "Do not add a citation when you are not sure. "
    "When you do answer, cite EVERY section you used, like (Section 1.1, Section 3.2)."
)


def ask(question):
        """Send the document plus a question to the LLM and return its answer."""
        response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": RULES},
                    {"role": "user", "content": f"DOCUMENT:\n{DOCUMENT}\n\nQUESTION: {question}"},
                ]
        )
        return response.choices[0].message.content

print("Q1:", ask("What is the minimum age to open an account?"))
print("Q2:", ask("What is the interest rate on savings accounts?"))
print("Q3:", ask("Can a 17-year-old open a Business Account if they have PKR 30,000?"))