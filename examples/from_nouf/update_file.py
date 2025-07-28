import re
from view_file import view_all_feedbacks

def update_feedbacks(feedbackSystem):
    if not feedbackSystem:
        print("Nothing to update.")
        return

    view_all_feedbacks(feedbackSystem)

    try:
        i = int(input("write the feedback you want to update:"))
        if 1 <= i <= len(feedbackSystem):
            new_feedback = input("Write your updated feedback: ").strip()
            if new_feedback:
                feedbackSystem[i - 1] = new_feedback
                print("Feedback updated")
            else:
                print("feedback is empty")
        else:
            print("Invalid number")
    except ValueError:
        print("Please enter a number")