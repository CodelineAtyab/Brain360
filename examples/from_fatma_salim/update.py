from view import view_feedback

def update_feedback(feedback_list):
    view_feedback(feedback_list)
    try:
        num = int(input("Enter number to update: ")) - 1
        if 0 <= num < len(feedback_list):
            new_fb = input("Enter new feedback: ")
            feedback_list[num] = new_fb
            print("Updated.")
        else:
            print("Invalid number.")
    except:
        print("Enter a valid number.")

if __name__ == "__main__":
    sample = ["Good job"]
    update_feedback(sample)
    print(sample)