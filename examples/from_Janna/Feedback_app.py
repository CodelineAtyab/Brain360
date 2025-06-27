import os
import re

file_path = r"C:\Users\bbuser\Desktop\Brain360\examples\from_Janna\feedback_data.txt"

def load_feedback(filepath):
    feedbacks = []
    try:
        with open(filepath, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    feedbacks.append(line)
    except FileNotFoundError:
        print("Feedback File Not Found!")
    return feedbacks

def save_feedback(filepath, entries):
    with open(filepath,"w") as file:
        for item in entries:
            file.write(item + "\n")

def display_feedback(feedbacks):
    if not feedbacks:
        print("There is no Feedback!")
        return
    print("Feedback Entries:")
    index = 1
    for feedback in feedbacks:
        print(f"{index}. {feedback}")
        index += 1
    print()

def add_feedback(feedbacks):
    while True:
        new_feedback = input("Kindly Enter Your Feedback or 'quit' to cancel: ").strip()
        if new_feedback.lower() == "quit":
            break
        if re.fullmatch(r"[A-Za-z0-9\s.,!?'-]+", new_feedback):
            feedbacks.append(new_feedback)
            print("Feedback Added!")
        else:
            print("Invalid Input! Please Enter Correct Characters.")

def update_feedback(feedbacks):
    if not feedbacks:
        print("No Feedback to Modify!")
        return
    display_feedback(feedbacks)

    while True:
        option = input("Choose a Feedback to Modify or 'quit' to cancel: ").strip()
        if option.lower() == "quit":
            break
        try:
            number = int(option) - 1
        except ValueError:
            print("Please Enter a Valid Number!")
            continue
        if number < 0 or number >= len(feedbacks):
            print("Invalid Number!")
            continue
        print(f"Current {feedbacks[number]}")
        new_feedback = input("Enter New Feedback").strip()

        if re.fullmatch(r"[A-Za-z0-9\s.,!?'-]+", new_feedback):
            feedbacks[number] = new_feedback
            print("Feedback Updated!")
        else:
            print("Invalid Input! Please Enter Correct Characters.")

def remove_feedback(feedbacks):
    if not feedbacks:
        print("No Feedback to Remove!")
        return
    display_feedback(feedbacks)
    while True:
        option = input("Enter feedback number to delete or 'quit' to cancel: ").strip()
        if option.lower() == "quit":
            break
        
        try:
            number = int(option) - 1
        except ValueError:
            print("Please Enter a Valid Number!")
            continue
        if number < 0 or number >= len(feedbacks):
            print("Invalid Number!")
            continue
        deleted = feedbacks.pop(number)
        print(f"Removed {deleted}")
        break

def run_app():
        feedback_entries = load_feedback(file_path)
        while True:
            print("Welcome to Feedback System:")
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
        save_feedback(file_path,feedback_entries)
        print("All Feedback Saved! Thank You :D")

if __name__ == "__main__":
    run_app()