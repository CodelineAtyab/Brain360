def display_feedback(feedbacks):
    if not feedbacks:
        print("There is no Feedback!")
        return
    print("Feedback Entries:")
    for index, feedback in enumerate(feedbacks, 1):
        print(f"{index}. {feedback}")
    print()

if __name__ == "__main__":
    display_feedback(["Good", "Could be better"])