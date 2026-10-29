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

def chunk_by_section(DOCUMENT):
    """ Make one Chunk for every line that starts with a number"""
    chunks = []
    lines = DOCUMENT.split("\n")

    for line in lines:
        if line!="" and line[0].isdigit():
            parts = line.split(" ", 1)
            chunk = {"section": "Section "+ parts[0], "text": parts[1]}
            chunks.append(chunk)

    return chunks
chunks = chunk_by_section(DOCUMENT)

print("Number of Chunks:", len(chunks))

for chunk in chunks: 
    print(chunk)