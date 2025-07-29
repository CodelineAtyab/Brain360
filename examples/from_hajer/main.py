# file operations
import json

FEEDBACK_FILE = "feedback_data.json"

def load_feedback():
    try:
        with open(FEEDBACK_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Corrupted feedback file. Starting with an empty list.")
        return []
    except Exception as e:
        print(f"Error loading feedback: {e}")
        return []

def save_feedback(feedback_entries):
    try:
        with open(FEEDBACK_FILE, "w") as f:
            json.dump(feedback_entries, f, indent=2)
    except Exception as e:
        print(f"Error saving feedback: {e}")


# core_Feedback.py
from feedback_view import view_feedback
from feedback_add import add_feedback
from feedback_update import update_feedback
from feedback_delete import delete_feedback
from feedback_data import feedback_entries

def main_menu():
    while True:
        print("""
===== Feedback Manager =====
1. View Feedback
2. Add Feedback
3. Update Feedback
4. Delete Feedback
5. Exit
============================
        """)
        choice = input("Select an option (1-5): ").strip()
        if choice == "1":
            view_feedback()
        elif choice == "2":
            add_feedback()
        elif choice == "3":
            update_feedback()
        elif choice == "4":
            delete_feedback()
        elif choice == "5":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid option. Please select from 1 to 5.")

if __name__ == "__main__":
    print("Loading feedback system...")
    print(f"Loaded {len(feedback_entries)} feedback entries.")
    main_menu()