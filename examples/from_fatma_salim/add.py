from storage import save_feedback

def add_feedback(feedback_list):
    fb = input("Enter feedback: ").strip()
    if fb:
        feedback_list.append(fb)
        save_feedback(feedback_list)
        print("✅ Feedback added.")
    else:
        print("❌ Invalid input.")
