# add feedback
from feedback_data import feedback_entries
from utils import validate_feedback

def add_feedback():
    feedback = input("Enter your feedback (numeric only): ").strip()
    if validate_feedback(feedback):
        feedback_entries.append(feedback)
        print("Feedback added successfully.")
    else:
        print("Invalid input. Only alphanumeric characters and spaces are allowed.")

if __name__ == "__main__":
    add_feedback()
