import os

def view_feedback(system_feedback):
    if not system_feedback:
        print("Nothing to view")
    else:
        for text, feedback in enumerate(system_feedback):
            print(f"{text}. {feedback}")