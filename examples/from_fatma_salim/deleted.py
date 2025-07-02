from view import view_feedback

def delete_feedback(feedback_list):
    view_feedback(feedback_list)
    try:
        num = int(input("Enter number to delete: ")) - 1
        if 0 <= num < len(feedback_list):
            feedback_list.pop(num)
            print("Deleted.")
        else:
            print("Invalid number.")
    except:
        print("Enter a valid number.")

if __name__ == "__main__":
    sample = ["Good job", "Needs improvement"]
    delete_feedback(sample)
    print(sample)