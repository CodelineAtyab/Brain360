from view_file import feedback_viewing

def feedback_deleted (the_feedback_system):# name of file 
    if not the_feedback_system:
        print("no feedback to be deleted")
        return
    feedback_viewing (the_feedback_system)



    try:
         updating_view= int(input("pls enter the feedback in order to delete: "))
         if 1<= updating_view <= len(the_feedback_system):
              deleted_feedback= the_feedback_system.pop(updating_view-1)
              print (f"delet it: {deleted_feedback}")
         else:
              print("try once agian")
    except ValueError:
              
              print("enter corret num")



