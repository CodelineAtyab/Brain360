import store_feedback
from view_feedback import view

def delete():
    entries = store_feedback.get_all_feedback()
    if not entries:
        print("No feedback to delete.")
        return

    view()
    index = int(input("Enter feedback ID to delete: ")) - 1
    if store_feedback.delete_feedback(index):
        print("Feedback deleted successfully!")
    else:
        print(f"Error: Invalid feedback ID. Please enter a number between 1 and {len(entries)}.")
if __name__ == "__main__":
    delete()