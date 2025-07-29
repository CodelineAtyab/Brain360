import os  

def View_the_Feedbacks(Feedback_Management_System):
    if not Feedback_Management_System:
        print("There are no feedbacks to view it")
    else:
        print("\n----Anonymous Feedback System----")
        print("\nAll FeedBacks:")
        for number, feedback in enumerate(Feedback_Management_System, start=1):
            print(f"{number}.{feedback}")


