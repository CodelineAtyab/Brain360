from view import view_feedback
from storage import save_feedback

def delete_feedback(feedback_list):
    view_feedback(feedback_list)
    try:
        num = int(input("Enter number to delete: ")) - 1
        if 0 <= num < len(feedback_list):
            feedback_list.pop(num)
            save_feedback(feedback_list)
            print("✅ Deleted.")
        else:
            print("❌ Invalid number.")
    except:
        print("❌ Enter a valid number.")
