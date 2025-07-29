# feedback view
from feedback_data import feedback_entries

def view_feedback():
    if not feedback_entries:
        print("No feedback entries available.")
    else:
        print(f"Showing {len(feedback_entries)} feedback entries:")
        for i, entry in enumerate(feedback_entries, start=1):
            print(f"{i}. {entry}")

if __name__ == "__main__":
    view_feedback()