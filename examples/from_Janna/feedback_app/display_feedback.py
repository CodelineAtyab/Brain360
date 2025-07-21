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

if __name__ == "__main__":
    display_feedback(["Good", "Could be better"])