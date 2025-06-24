from file_utils import load_feedback, save_feedback

def delete_feedback(feedback_list):
    feedback_list = load_feedback()
    if not feedback_list:
        print("No feedback to delete")
        return

    for i, feedback in enumerate(feedback_list, 1):
        print(f"{i} {feedback}")

    try:
        print("You are going to delete a value permenatly")
        num = int(input("Enter a number to delete "))
        if 1 <= num <= len(feedback_list):
            removed = feedback_list.pop(num - 1)
            save_feedback(feedback_list)
            print(f"{removed} has been deleted from your feedback")
        else:
            print("Invalid")
    except:
        print("Aright dude enter a valid number: ")


