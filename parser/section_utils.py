import re

def detect_section(line: str):
    line = line.strip()

    if len(line) < 4:
        return None

    # ignore single word headers like "SVD"
    if len(line.split()) == 1:
        return None

    # numbered section like "1 Introduction"
    if re.match(r"^\d+(\.\d+)*\s+[A-Z]", line):
        return line

    # heading in Title Case and short
    if line.istitle() and len(line.split()) <= 8:
        return line

    # ALL CAPS but not too short
    if line.isupper() and len(line.split()) > 1 and len(line.split()) < 10:
        return line

    return None
