import re
def add_feedback(feedbackSystem):
    insert = input("Enter your feedback: ").strip()
    if re.fullmatch(r"[A-Za-z0-9]+", insert):
        feedbackSystem.append(insert)
        print("The Feedback added successfully")
    else:
        print("Try Again")