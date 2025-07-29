# main
from add_feedback import add_feedback
from view_feedback import view_feedback
from update_feedback import update_feedback
from delete_feedback import delete_feedback

def show_menu():
    print("\n=== Feedback Manager ===")
    print("1. View Feedback")
    print("2. Add Feedback")
    print("3. Update Feedback")
    print("4. Delete Feedback")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Select an option (1–5): ").strip()

        if choice == "1":
            view_feedback()
        elif choice == "2":
            add_feedback()
        elif choice == "3":
            update_feedback()
        elif choice == "4":
            delete_feedback()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 5.")

if __name__ == "__main__":
    main()
