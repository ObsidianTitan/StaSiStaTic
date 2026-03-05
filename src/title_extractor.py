def extract_title(markdown):
    lines = markdown.splitlines()
    
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
            continue

    raise Exception("title need a header")

