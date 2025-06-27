feedback=[]

while True:
    print(" \n the service that we have: ")
    print("1. View all feedback")
    print("2. Add new feedback")
    print("3. Update feedback")
    print("4. Delete feedback")
    print("5. Exit")
    service = int(input("what do you want to do(chouse one from 1 to 5): "))  
    if service ==1 :
        print( "\n"      ,feedback)
    if service== 2 :
            while True:
                added_feedback =input("what do you want to added (or write done to exit): ")
                if added_feedback != "done":
                    feedback.append(added_feedback)
                else:
                    print("\n your feedback is: ", feedback)
                    break
    if service==4 :
        delete_feedback = input("write what do you want to delet :")
        if delete_feedback in feedback:
            feedback.remove(delete_feedback)
        else:
         print("this feedback is not in the list: ")
    if service == 5:
        feedback.clear()
        print("the feedback list is cleared")



         
         
