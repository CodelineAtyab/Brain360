from add_feedback import add_feedback
from view_feedback import view_feedback
from update_feedback import update_feedback
from del_feedback import delete_feedback

feedback_list = []

def display_menu():
    print("Anonymous Feedback System")
    print("1. View all feedback")
    print("2. Add new feedback")
    print("3. Update feedback")
    print("4. Delete feedback")
    print("5. Exit")
    print("6. To view what each prompt does")

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            view_feedback(feedback_list)
        elif choice == "2":
            add_feedback(feedback_list)
        elif choice == "3":
            update_feedback(feedback_list)
        elif choice == "4":
            delete_feedback(feedback_list)
        elif choice == "5":
            print("Program closed, bye user")
        elif choice == "6":
            print("(1) lets you view the list")
            print("(2) lets you add value to the list")
            print("(3) lets you update one of the values to a newer one")
            print("(4) lets you delete a value from the list")
            break
        else:
            print("Invalid")
            print("You have to choose a number from 1 to 5 " \
            "for example (1) will let you view the list")
