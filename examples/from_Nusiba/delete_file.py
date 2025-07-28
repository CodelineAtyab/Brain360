from view_file import view_feedback

def delete_feedback(system_feedback):
    if not system_feedback:
        print("Nothing to update")
        return 
    view_feedback(system_feedback)

    try: 
        user_input = int(input("Enter the feedback to delete:")) 
        if 1 <= user_input <= len(system_feedback):
           Delete = system_feedback.pop(user_input - 1)
           print(f"Delete: {Delete}")

        else:
            print("Try Again")

    except ValueError:
        print("Enter the right number")
    

    
                                                              



