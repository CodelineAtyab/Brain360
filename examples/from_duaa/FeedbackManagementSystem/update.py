import re
import view
def update(feedlist):
    print("\n****(Update Feedback)****")
    if not feedlist:
        print("List is empty Nothing to update\n")
        return
    view.view(feedlist)
    try:
        num = (input("Enter the number of feedback to update: or (Cancel) ")).strip()
        if num.lower() == 'cancel':
            print("Cancelled.\n")
            return 
        num = int(num)
        if 1 <= num <= len(feedlist):
            new_feedback = input("Enter the update: ").strip()
            if not new_feedback:
                print("Error: Feedback cannot be empty\n")
                return
            if re.search(r"[^\w ]", new_feedback):  
                print("Error Only letters, numbers and spaces allowed\n")
            else:
                feedlist[num - 1] = new_feedback
                print("Updated successfully!\n")
        else:
            print("Error Invalid Feedback Number\n")
    except ValueError:
        print("Error Enter Valid Number\n")
if __name__ == "__main__":
    test3 = [6, "test"]
    update(test3)
    print(test3)


