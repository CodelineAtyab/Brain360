from file_utils import load_feedback, save_feedback


def add_feedback(feedback_list):
    feedback_list = load_feedback() 
    feedback = input("Enter the feedback you desire: ")
    feedback_list.append(feedback)
    save_feedback(feedback_list)
    print("Feedback added, youre good to go.")
