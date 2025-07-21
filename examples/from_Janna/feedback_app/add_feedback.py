from validation import is_valid_feedback

def add_feedback(feedbacks):
    while True:
        new_feedback = input("Kindly Enter Your Feedback or 'quit' to cancel: ").strip()
        if new_feedback.lower() == "quit":
            break
        if is_valid_feedback(new_feedback):
            feedbacks.append(new_feedback)
            print("Feedback Added!")
        else:
            print("Invalid Input! Please Enter Correct Characters.")

if __name__ == "__main__":
    test_list = []
    add_feedback(test_list)
    print(test_list)