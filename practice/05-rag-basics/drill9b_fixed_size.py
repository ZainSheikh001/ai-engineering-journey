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


def chunk_fixed(text, size, overlap):
    """Cut text into pieces of `size` characters that share `overlap` characters."""
    chunks = []
    for start in range(0, len(text), size - overlap):
        chunk = text[start:start + size]
        chunks.append(chunk)
        if start + size >= len(text):
            break
    return chunks


chunks = chunk_fixed(DOCUMENT, 60, 15)

print("Number of chunks:", len(chunks))
for chunk in chunks:
    print("CHUNK:", chunk)
    print("-" * 30)