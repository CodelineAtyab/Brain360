# core feedback
from feedback_view import view_feedback
from feedback_add import add_feedback
from feedback_update import update_feedback
from feedback_delete import delete_feedback

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
    from feedback_data import feedback_entries
    print("Loading feedback system...")
    print(f"Loaded {len(feedback_entries)} feedback entries.")
    main_menu()