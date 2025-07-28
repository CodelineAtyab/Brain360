from view_file import feedback_viewing   #view_file function
import re 
def feedback_updating (the_feedback_system):# name of file 
    if not the_feedback_system:
        print("no feedback to be printed")
        return
    feedback_viewing (the_feedback_system)

    #update and delete i will add #try (checks my code) #except (handles the error if its not there)
    #no need to use it 

    
    updating_view= int(input("pls enter the feedback in order to update: "))

    if 1<= updating_view <= len(the_feedback_system):
        feedback_to_update= input("enter new feed: "). strip()
        if re.fullmatch(r"[A-Za-z0-9]+",feedback_to_update):
            the_feedback_system[updating_view-1] = feedback_to_update
            print ("feedback successfully updated")
    else:
        print("try once agian")





