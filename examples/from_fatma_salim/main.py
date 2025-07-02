from core_feedback_menu import show_menu
from view import view_feedback
from add import add_feedback
from update import update_feedback
from deleted import delete_feedback

feedback_list = []

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Choose 1-5: ")

        if choice == '1':
            view_feedback(feedback_list)
        elif choice == '2':
            add_feedback(feedback_list)
        elif choice == '3':
            update_feedback(feedback_list)
        elif choice == '4':
            delete_feedback(feedback_list)
        elif choice == '5':
            print("Bye!")
            break
        else:
            print("Try again.")