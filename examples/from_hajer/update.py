# update feedback
from feedback_data import feedback_entries
from utils import validate_feedback

def update_feedback():
    if not feedback_entries:
        print("No feedback entries to update.")
        return

    try:
        idx = int(input("Enter the feedback number to update: ")) - 1
        if 0 <= idx < len(feedback_entries):
            new_feedback = input("Enter new feedback: ").strip()
            if validate_feedback(new_feedback):
                feedback_entries[idx] = new_feedback
                print("Feedback updated successfully.")
            else:
                print("Invalid input. Only alphanumeric characters and spaces are allowed.")
        else:
            print("Invalid feedback number.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    update_feedback()
