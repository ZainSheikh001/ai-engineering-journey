from sentence_transformers import SentenceTransformer, util

# ---------- RETRIEVAL: top-k retriever ----------
model = SentenceTransformer("all-MiniLM-L6-v2")
chunks = chunk_with_context(DOCUMENT, "Example Microfinance Bank Account Opening Policy", "2026-01-01")

# Encode every chunk ONCE, up front
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