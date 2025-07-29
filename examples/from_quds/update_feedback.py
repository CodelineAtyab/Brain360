from view_feedbacks import View_the_Feedbacks
import re

def Update_a_Feedback(Feedback_Management_System):
    if not Feedback_Management_System:
        print("There Are No Feedbacks To  Update")
        return
    View_the_Feedbacks(Feedback_Management_System)

    try:
        choices_op = int(input("Enter Feedback ID to update: "))
        if 1 <= choices_op <= len(Feedback_Management_System):
            Updated_Feedback =input("Please Eneter The New Feedback: ").strip()
            if re.fullmatch(r"[A-za-z0-9 !]+",Updated_Feedback):
                Feedback_Management_System[choices_op - 1] = Updated_Feedback
                print("Feedback updated successfully!")
            else:
                print("Error: Feedback can only contain alphanumeric characters and spaces.")
        else:
            print(f"Error: Invalid feedback ID. Please enter a number between 1 and {len(Feedback_Management_System)}")

    except ValueError:
        print("Please Enter The Right ID Number To Update")

        # print("Please Enter The Right Number")



