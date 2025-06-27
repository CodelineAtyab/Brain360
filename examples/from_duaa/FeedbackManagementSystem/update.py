import re
import view
def update(feedlist):
    if not feedlist:
        print("List is empty\n")
        return
    view.view(feedlist)
    try:
        num = int(input("Enter the number of feedback to update: "))
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
            print("Error\n")
    except ValueError:
        print("Error\n")
if __name__ == "__main__":
    test3 = [6, "test"]
    update(test3)
    print(test3)


