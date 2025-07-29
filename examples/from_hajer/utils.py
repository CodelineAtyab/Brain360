
import re

def validate_feedback(text):
    """
    Validates that the input contains only alphanumeric characters and spaces.
    """
    return bool(re.fullmatch(r"[A-Za-z0-9\s]+", text.strip()))
