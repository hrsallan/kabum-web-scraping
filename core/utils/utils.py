import re

def normalize_title_to_link(title: str) -> str:
    normalized = re.sub(r"[^a-zA-Z0-9\s-]", "", title)
    normalized = normalized.replace(" ", "-")
    normalized = re.sub(r"-{2,}", "-", normalized)
    normalized = normalized.lower()
    normalized = normalized.strip("-")
    return normalized