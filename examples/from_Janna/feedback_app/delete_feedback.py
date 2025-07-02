from display_feedback import display_feedback

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
            if 0 <= number < len(feedbacks):
                deleted = feedbacks.pop(number)
                print(f"Removed: {deleted}")
                break
            else:
                print("Invalid Number!")
        except ValueError:
            print("Please Enter a Valid Number!")

if __name__ == "__main__":
    test_fb = ["Item A", "Item B"]
    remove_feedback(test_fb)
    print(test_fb)