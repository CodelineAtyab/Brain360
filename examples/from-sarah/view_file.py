import os

def feedback_viewing (the_feedback_system):# name of file 
    if not the_feedback_system:
        print("no feedback to be printed")
    else:
        print("\n feedback system")
        for num, feedback in enumerate (the_feedback_system):
            print (f"{num}.{feedback}")
    

    # to link to the main
