import os
from view_file import view_feedback
from add_file import add_feedback
from update_file import update_feedback
from delete_file import delete_feedback

path = "C:\\Users\\bbuser\\Desktop\\Brain360\\examples\\from_nusiba\\text_file.txt"

# load function: loading feedback ---> using method read (r)

def load_feedback():
    if not os.path.exists(path):
        return []
    
    try:
        with open(path, "r") as file:
            return [line.strip() for line in file.readlines()]
        
    except IOError:
        print("Not found")
        return []
    
# save function: to save the feedback , to save any modification in a feedbacks

def save_feedback(New_feedback_list): 
    try:
        with open(path, "w") as file:
            for feedback in New_feedback_list:
                file.write(feedback + "\n")
        
    except IOError:
        print("There is an Error to writing to the file")
        

def main_feedback():
    system_feedback = load_feedback()

    while True:
        print("\nWelcome to Feedback Management System")
        print("1. view feedback")
        print("2. add feedback")
        print("3. update feedback")
        print("4. delete feedback")
        print("5. exit")
    
        user_input = input("What do you want to do? ").lower()

        if user_input == "1":
            view_feedback(system_feedback)
        elif user_input == "2":
            add_feedback(system_feedback)
            save_feedback(system_feedback)
        elif user_input == "3":
            update_feedback(system_feedback)
            save_feedback(system_feedback)
        elif user_input == "4":
            delete_feedback(system_feedback)
            save_feedback(system_feedback)
        elif user_input == "5":
            print("Exit")
            break
        else:
            print("Try Again")
    
if __name__ == "__main__":
    main_feedback()




