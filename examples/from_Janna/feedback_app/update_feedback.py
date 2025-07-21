from validation import is_valid_feedback
from display_feedback import display_feedback

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
            if 0 <= number < len(feedbacks):
                print(f"Current: {feedbacks[number]}")
                new_feedback = input("Enter New Feedback: ").strip()
                if is_valid_feedback(new_feedback):
                    feedbacks[number] = new_feedback
                    print("Feedback Updated!")
                    break
                else:
                    print("Invalid Input! Please Enter Correct Characters.")
            else:
                print("Invalid Number!")
        except ValueError:
            print("Please Enter a Valid Number!")

if __name__ == "__main__":
    test_fb = ["Good", "Okay"]
    update_feedback(test_fb)