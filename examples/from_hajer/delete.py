# delete_feedback.py
from feedback_data import feedback_entries

def delete_feedback():
    if not feedback_entries:
        print("No feedback entries to delete.")
        return

    try:
        idx = int(input("Enter the feedback number to delete: ")) - 1
        if 0 <= idx < len(feedback_entries):
            deleted = feedback_entries.pop(idx)
            print(f"Feedback deleted: \"{deleted}\"")
        else:
            print("Invalid feedback number.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    delete_feedback()
