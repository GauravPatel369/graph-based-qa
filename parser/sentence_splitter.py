import re
from nltk.tokenize import sent_tokenize

def clean_text(text: str) -> str:
    """
    Remove weird spacing and artifacts.
    """
    text = re.sub(r"\s+", " ", text)
    text = text.replace("\n", " ")
    return text.strip()


def split_into_sentences(text: str):
    text = clean_text(text)
    sentences = sent_tokenize(text)
    return [s.strip() for s in sentences if len(s.strip()) > 3]
