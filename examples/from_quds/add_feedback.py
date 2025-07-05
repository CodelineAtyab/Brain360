import re

def Add_the_Feedback(Feedback_Management_system):
    Adding_a_Feedback = input("Please Enter Your Feedback: ").strip()
    if re.fullmatch(r"[A-za-z0-9 !]+",Adding_a_Feedback):
        Feedback_Management_system.append(Adding_a_Feedback)
        print("Feedback added successfully!")
    else:
        print("Error: Feedback can only contain alphanumeric characters and spaces.")



