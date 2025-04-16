import re


def split_score_string(s: str) -> tuple:
    """
    Split a team-score string into the team name and score.

    Expects a string in the format: "<team_name> <score>".
    Handles team names with spaces. Example: "FC Awesome 3" → ("FC Awesome", "3")

    Args:
        s (str): A string containing a team name followed by a score.

    Returns:
        tuple: A tuple containing (team_name: str, score: str).

    Raises:
        ValueError: If the input string is not in the expected format.
    """
    match = re.match(r'^(.*\S)\s+(\d+)$', s.strip())
    if match:
        return match.groups()
    else:
        raise ValueError("Not valid score in game string")
