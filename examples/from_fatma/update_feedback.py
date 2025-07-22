import re
import store_feedback
from view_feedback import view

def update():
    entries = store_feedback.get_all_feedback()
    if not entries:
        print("No feedback to update.")
        return
    view()
    feedback_id = int(input("Enter feedback ID to update: "))-1
    if 0 <= feedback_id < len(entries):
        print(f"Current feedback: {entries[feedback_id]}")
        new_feedback = input("Enter new feedback: ")
        if re.match(r'^[a-zA-Z0-9 ]+$', new_feedback):
            new_feedback.strip()
            store_feedback.update_feedback(feedback_id, new_feedback)
            print("Feedback updated successfully!")
        else:
            print("Error: Feedback can only contain alphanumeric characters and spaces.")
    else:
        print(f"Error: Invalid feedback ID. Please enter a number between 1 and {len(entries)}.")

if __name__=="__main__":
    update()