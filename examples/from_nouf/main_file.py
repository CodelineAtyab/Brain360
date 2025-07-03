import os
from view_file import view_all_feedbacks
from add_file import add_feedback
from update_file import update_feedbacks
from delete_file import delete_feedback


path_file = "C:\\Users\\bbuser\\Desktop\\360\\Brain360\\examples\\from_nouf\\text_file.txt"

def load_feedbacks():
    if os.path.exists(path_file):
        with open(path_file, "r") as file:
            return [line.strip() for line in file if line.strip()]
    return []

def save_feedbacks(feedbacks_list):
    with open(path_file, "w") as file:
        for feedback in feedbacks_list:
            file.write(feedback + "\n")




def Feedback_main():
     feedbackSystem = load_feedbacks()

     while True:
        print("1. view your feedbacks")

        print("2. add your feedback")

        print("3. update feedbacks")

        print("4. delete feedbacks")
        
        print("5. Exit")

        input1 = input("Choose from these options: ").strip()

        if input1 == "1":
           view_all_feedbacks(feedbackSystem)
        elif input1 == "2":
           add_feedback(feedbackSystem)
           save_feedbacks(feedbackSystem)
        elif input1 == "3":
           update_feedbacks(feedbackSystem)
           save_feedbacks(feedbackSystem)
        elif input1 == "4":
           delete_feedback(feedbackSystem)
           save_feedbacks(feedbackSystem)
        elif input1 == "5":
           print("Bye!")
           break
        else:
           print("Invalid choice. Please enter a number from 1 to 5.\n")


if __name__=="__main__":
    Feedback_main()