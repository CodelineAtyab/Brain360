from file_utils import load_feedback, save_feedback

def update_feedback(feedback_list):
    feedback_list = load_feedback()
    if not feedback_list:
        print("Sorry bruh, but there is nothing to update")
        return
    for i, feedback in enumerate(feedback_list, 1):
        print(f"{i}. {feedback}")
    try:
        num = int(input("which number would ya like to update: "))
        if 1 <= num <= len(feedback_list):
            new_fb = input("New feedback: ")
            feedback_list[num - 1] = new_fb
            save_feedback(feedback_list)
            print("Updated!")
        else:
            print("invalid")
    except:
        print("Enter a number!!!!!!!: ")

