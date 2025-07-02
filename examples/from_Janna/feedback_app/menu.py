from add_feedback import add_feedback
from display_feedback import display_feedback
from update_feedback import update_feedback
from delete_feedback import remove_feedback
from file_io import load_feedback, save_feedback

file_path = r"C:\Users\bbuser\Desktop\ML\feedback_data.txt"

def run_app():
    feedback_entries = load_feedback(file_path)

    while True:
        print("\n--- Anonymous Feedback System ---")
        print("1. Add Feedback")
        print("2. Display Feedback")
        print("3. Edit Feedback")
        print("4. Delete Feedback")
        print("5. Exit")

        user_option = input("Select an Option: ").strip()

        if user_option == "1":
            add_feedback(feedback_entries)
        elif user_option == "2":
            display_feedback(feedback_entries)
        elif user_option == "3":
            update_feedback(feedback_entries)
        elif user_option == "4":
            remove_feedback(feedback_entries)
        elif user_option == "5":
            break
        else:
            print("Invalid Option!")

    save_feedback(file_path, feedback_entries)
    print("All Feedback Saved! Thank You :D")