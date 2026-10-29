from sentence_transformers import SentenceTransformer, util

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


# ---------- CHUNKER (copied from drill 9c) ----------
def chunk_with_context(document, source, date):
    """One chunk per rule, with its heading and where it came from."""
    chunks = []
    heading = ""
    for line in document.split("\n"):
        if line.startswith("Section"):
            heading = line
        elif line != "" and line[0].isdigit():
            parts = line.split(" ", 1)
            chunks.append({
                "section": "Section " + parts[0],
                "text": heading + " > " + parts[1],
                "source": source,
                "date": date,
            })
    return chunks


# ---------- RETRIEVAL: top-k retriever ----------
model = SentenceTransformer("all-MiniLM-L6-v2")
chunks = chunk_with_context(DOCUMENT, "Example Microfinance Bank Account Opening Policy", "2026-01-01")

chunk_texts = []
for chunk in chunks:
    chunk_texts.append(chunk["text"])
chunk_vecs = model.encode(chunk_texts)


def retrieve(question, top_k):
    """Return the top_k chunks whose meaning is closest to the question."""
    q_vec = model.encode(question)
    scores = util.cos_sim(q_vec, chunk_vecs)[0]
    results = []
    for i in range(len(chunks)):
        results.append({
            "score": round(float(scores[i]), 3),
            "section": chunks[i]["section"],
            "text": chunks[i]["text"],
        })
    results = sorted(results, key=lambda r: r["score"], reverse=True)
    return results[:top_k]


# ---------- RUN ----------
questions = [
    "What is the minimum age to open an account?",
    "What documents do I need to bring?",
    "How much money must a business account hold?",
]

for q in questions:
    print("QUESTION:", q)
    for r in retrieve(q, 2):
        print("   ", r["score"], r["section"], "|", r["text"])
    print("-" * 40)