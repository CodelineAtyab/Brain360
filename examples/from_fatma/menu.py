import view_feedback
import add_feedback
import update_feedback
import delete_feedback
import exit_feedback

def menu():
    feedback = True
    while feedback:
        print("--- Anonymous Feedback System ---")
        print("1. View all feedback\n2. Add new feedback\n" \
        "3. Update feedback\n4. Delete feedback\n5. Exit")

        choice = int(input("Enter your choice: "))
        if choice==1:
            view_feedback.view()
        elif choice==2:
            add_feedback.add()
        elif choice==3:
            update_feedback.update()
        elif choice==4:
            delete_feedback.delete()
        elif choice==5:
            exit_feedback.exit_funcion()
        else:
            print("Choose from 1 to 5 only.")

if __name__ == "__main__":
    menu()