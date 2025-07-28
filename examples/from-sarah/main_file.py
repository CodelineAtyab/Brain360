import os 
from view_file import feedback_viewing 
from add_file import add
from update_file import feedback_updating
from delete_file import feedback_deleted  

#to update the feedback copied the path of feedback.txt
path_of_file = "C:\\Users\\bbuser\\Documents\\Brain360\\examples\\from-sarah\\file_feedback.txt"  

# read
def load_feedback():
    if not os.path.exists(path_of_file):
        return[]
    try:
        with open (path_of_file, "r") as file:
            return [line.strip() for line in file.readlines()]
        
    except IOError:
        print("data not found")
        return []
    

#write
def feedback_to_save(new_feedback_system):
    try:
        with open (path_of_file, "w") as file:
            for list_of_feedback in new_feedback_system:
                file.write(list_of_feedback+"\n")

        
    except IOError:
        print("data of writings were not found ")
   
    
    #main

def main_feed():
    the_feedback_system = load_feedback()
    while True:
        print()
        print("1. view feedback")
        print("2. add feedback")
        print("3. update feedback")
        print("4. delete feedback")
        print("5. Exit")
        
        updating_view = input("Choose an option: ")

        if updating_view == "1":
            feedback_viewing(the_feedback_system)      #no need to save here


        elif updating_view == "2":
            add(the_feedback_system)
            feedback_to_save(the_feedback_system)
        

        elif updating_view == "3":
            feedback_updating(the_feedback_system)
            feedback_to_save(the_feedback_system)

        elif updating_view == "4":
            feedback_deleted(the_feedback_system)
            feedback_to_save(the_feedback_system)

        elif updating_view == "5":
            print("You have exit from the system")
            break

        else:
            print("Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main_feed()

        


