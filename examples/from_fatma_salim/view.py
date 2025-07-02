def view_feedback(feedback_list):
    if not feedback_list:
        print("No feedback yet.")
    else:
        print("\nFeedback List:")
        for i, feedback in enumerate(feedback_list, 1):
            print(f"{i}. {feedback}")
