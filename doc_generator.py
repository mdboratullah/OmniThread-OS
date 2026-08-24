def get_documentation_index():
    """
    Indexes system guides, API specs, and security whitepapers.
    """
    docs = [
        "1. Quick Start Installation Guide",
        "2. Enterprise Administrator Manual",
        "3. REST API Developer Reference",
        "4. Security & Compliance Whitepaper"
    ]
    return docs

if __name__ == '__main__':
    for doc in get_documentation_index():
        print(doc)
