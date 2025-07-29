# feedback update
from feedback_data import feedback_entries
from utils import is_valid_feedback

def update_feedback():
    if not feedback_entries:
        print("No feedback entries to update.")
        return

    try:
        view_feedback()
        idx = int(input("Enter the ID of the feedback to update: "))
        if 1 <= idx <= len(feedback_entries):
            print(f"Current feedback: {feedback_entries[idx - 1]}")
            new_feedback = input("Enter new feedback (alphanumeric only): ").strip()
            if is_valid_feedback(new_feedback):
                feedback_entries[idx - 1] = new_feedback
                print("Feedback updated successfully.")
            else:
                print("Invalid input. Only alphanumeric characters and spaces allowed.")
        else:
            print("Invalid ID.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    from feedback_view import view_feedback
    update_feedback()