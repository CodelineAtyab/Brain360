from view import view_feedback
from storage import save_feedback

def update_feedback(feedback_list):
    view_feedback(feedback_list)
    try:
        num = int(input("Enter number to update: ")) - 1
        if 0 <= num < len(feedback_list):
            new_fb = input("Enter new feedback: ").strip()
            if new_fb:
                feedback_list[num] = new_fb
                save_feedback(feedback_list)
                print("✅ Updated.")
            else:
                print("❌ Empty feedback.")
        else:
            print("❌ Invalid number.")
    except:
        print("❌ Enter a valid number.")