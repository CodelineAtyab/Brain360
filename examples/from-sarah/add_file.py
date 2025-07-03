import re
def add(the_feedback_system):
    feedback = input("Enter feedback to add: ")
    if re.fullmatch(r"[A-Za-z0-9]+", feedback):       #so to make sure that number and text are validate 
         the_feedback_system.append(feedback)
         print("'" + feedback + "' added to the feedback list.")

