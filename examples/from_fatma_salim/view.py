def view_feedback(feedback_list): 
    if not feedback_list: 
        print("No feedback yet.") 
    else: 
        print("\nFeedback List:") 
        for i, feedback in enumerate(feedback_list, 1):
            print(i, feedback)

if __name__ == "__main__":
    sample = ["Test feedback"]
    view_feedback(sample)