import os

def view_all_feedbacks(feedbackSystem):
    if not feedbackSystem:
        print("Nothing to view. No feedbacks found.")
    else:
        print("Feedbacks:")
        for i, feedback in enumerate(feedbackSystem, start=1):
            print(f"{i}. {feedback}")