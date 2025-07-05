from view_feedbacks import View_the_Feedbacks

def Delete_the_feedback(Feedback_Management_System):
    if not Feedback_Management_System:
        print("There Are No Feedback To Deleted")
        return
    View_the_Feedbacks(Feedback_Management_System)

    try:
        choices_op = int(input("Please Enter The Number Of The Feedback To Delete: "))
        if 1 <= choices_op <= len(Feedback_Management_System):
            Delete_a_Feedback = Feedback_Management_System.pop(choices_op - 1)
            print(f"{Delete_a_Feedback}. Has been Deleted")
        else:
            print(f"Error: Invalid feedback ID. Please enter a number between 1 and {len(Feedback_Management_System)}")
    except ValueError:
        print("Please Enter The Right ID Number To Delete")




