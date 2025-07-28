from view_file import view_all_feedbacks
def delete_feedback(feedbackSystem):
    if not feedbackSystem:
        print("Nothing to delete")
        return
    view_all_feedbacks(feedbackSystem)
    try:
        input1 = int(input("Enter the feedback to delete:"))
        if 1 <= input1 <= len(feedbackSystem):
           Delete = feedbackSystem.pop(input1 -1)
           print(f"Delete: {Delete}")
        else:
            print("Try Again")
    except ValueError:
        print("Enter the right number")