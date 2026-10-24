from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq()  # reads GROQ_API_KEY from the environment automatically

MODEL = "openai/gpt-oss-20b"
QUESTION = "What does the State Bank of Pakistan do?"
RULES = "You are a compliance assistant for Pakistani banks. Answer in exactly 3 bullet points, maximum 50 words in total, in simple English. If you are not sure, say 'I am not sure.'"

# Call A: no system message (the model decides length and format itself)
response_a = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "user", "content": QUESTION},
    ],
)
print("CALL A:\n", response_a.choices[0].message.content)

# Call B: system message (rules) + user message (question)
response_b = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": RULES},
        {"role": "user", "content": QUESTION},   # ← ADDED: the question was missing
    ],
)
print("\nCALL B:\n", response_b.choices[0].message.content)