# feedback add
from feedback_data import feedback_entries
from utils import is_valid_feedback
from file_operations import save_feedback

def add_feedback():
    feedback = input("Enter feedback (alphanumeric only): ").strip()
    if is_valid_feedback(feedback):
        feedback_entries.append(feedback)
        save_feedback(feedback_entries)
        print("Feedback added successfully.")
    else:
        print("Invalid feedback. Only alphanumeric characters and spaces are allowed.")

if __name__ == "__main__":
    add_feedback()