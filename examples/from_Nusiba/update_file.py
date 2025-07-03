from view_file import view_feedback
import re

def update_feedback(system_feedback):
    if not system_feedback:
        print("Nothing to update.")
        return 

    view_feedback(system_feedback)

    try:
        user_input = int(input("Enter the feedback number to update: "))

        if 1 <= user_input <= len(system_feedback):
            Update = input("Enter your feedback: ").strip()

            # Validate input (letters and numbers only, no special chars)
            if re.fullmatch(r"[A-Za-z0-9 ]+", Update):
                system_feedback[user_input - 1] = Update
                print("The feedback was updated successfully.")
            else:
                print("Invalid input. Please use only letters, numbers, and spaces.")
        else:
            print(f"Invalid number. Please enter a number between 1 and {len(system_feedback)}.")

    except ValueError:
        print("Invalid input. Please enter a numeric value.")
