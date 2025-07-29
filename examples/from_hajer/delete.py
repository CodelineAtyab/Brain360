# feedback delete
from feedback_data import feedback_entries

def delete_feedback():
    if not feedback_entries:
        print("No feedback entries to delete.")
        return

    try:
        view_feedback()
        idx = int(input("Enter the ID of the feedback to delete: "))
        if 1 <= idx <= len(feedback_entries):
            deleted = feedback_entries.pop(idx - 1)
            print(f"Deleted feedback: {deleted}")
        else:
            print("Invalid ID.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    from feedback_view import view_feedback
    delete_feedback()