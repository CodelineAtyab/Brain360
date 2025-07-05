import os
from view_feedbacks import View_the_Feedbacks
from add_feedback import Add_the_Feedback
from update_feedback import Update_a_Feedback
from delete_feedback import Delete_the_feedback

file_name = "C:\\Users\\bbuser\\Desktop\\360\\Brain360\\examples\\from_quds\\file_text.txt"


def Loading_the_Feedbacks():
    if not os.path.exists(file_name):
        return[]
    try:
        with open(file_name, "r")as file:
            return[line.strip() for line in file.readlines()]
    except IOError:
        print("The Data Is Not Found")
        return[]
    
# def Loading_the_Feedbacks():
#     if not os.path.exists(file_name):
#         return []
#     try:
#         with open(file_name, "r", encoding="utf-8") as file:
#             return [line.strip() for line in file.readlines()]
#     except IOError:
#         print("The data is not found")
#         return []

    
def Saving_the_Feedbacks(Feedback_System_List):
    try:
        with open(file_name, "w") as file:
            for Feedbacks_list in Feedback_System_List:
                file.write(Feedbacks_list + "\n")
    except IOError:
        print("Error: Could not write to the file ")


def main():
    Feedback_Management_System = Loading_the_Feedbacks()

    while True:
        
        print("\n 1. Core Feedback Management System")
        print("1. View Feedback\n2. Add  Feedback\n3. Update Feedback\n4. Delete Feedback\n5. Exit")
        choices_op =input("Please Select on of the choices: ")

        if choices_op == "1":
            View_the_Feedbacks(Feedback_Management_System)
        elif choices_op == "2":
            Add_the_Feedback(Feedback_Management_System)
            Saving_the_Feedbacks(Feedback_Management_System)
        elif choices_op == "3":
            Update_a_Feedback(Feedback_Management_System)
            Saving_the_Feedbacks(Feedback_Management_System)
        elif choices_op == "4":
            Delete_the_feedback(Feedback_Management_System)
            Saving_the_Feedbacks(Feedback_Management_System)
        elif choices_op == "5":
            print("Exiting application. All feedback saved.")
            break
        else:
            print("Please try again")

if __name__ == "__main__":
    main()
