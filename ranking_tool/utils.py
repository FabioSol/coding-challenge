import re


def split_score_string(s: str) -> tuple:
    match = re.match(r'^(.*\S)\s+(\d+)$', s.strip())
    if match:
        return match.groups()
    else:
        raise ValueError("Not valid score in game string")
