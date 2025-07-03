import re

def is_valid_feedback(text):
    return bool(re.fullmatch(r"[A-Za-z0-9\s.,!?'-]+", text))

if __name__ == "__main__":
    print(is_valid_feedback("Valid feedback!"))
    print(is_valid_feedback("Invalid feedback"))