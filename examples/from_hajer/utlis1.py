# utils
import re

def is_valid_feedback(feedback):
    return bool(re.fullmatch(r"[A-Za-z0-9\s]+", feedback))