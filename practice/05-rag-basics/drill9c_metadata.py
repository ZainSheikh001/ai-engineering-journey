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


def chunk_with_context(document, source, date):
    """One chunk per rule, with its heading and where it came from."""
    chunks = []
    heading = ""

    for line in document.split("\n"):
        if line.startswith("Section"):
            heading = line
        elif line != "" and line[0].isdigit():
            parts = line.split(" ", 1)
            chunk = {
                "section": "Section " + parts[0],
                "text": heading + " > " + parts[1],
                "source": source,
                "date": date,
            }
            chunks.append(chunk)

    return chunks


chunks = chunk_with_context(DOCUMENT, "Example Microfinance Bank Account Opening Policy", "2026-01-01")

for chunk in chunks:
    print(chunk)