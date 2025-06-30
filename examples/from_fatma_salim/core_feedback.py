feedback_list = []

def show_menu():
    print("\n--- Feedback System ---")
    print("1. View Feedback")
    print("2. Add Feedback")
    print("3. Update Feedback")
    print("4. Delete Feedback")
    print("5. Exit")

def view_feedback(): 
    if not feedback_list: 
        print("No feedback yet.") 
    else: 
      print("\nFeedback List:") 
      i = 1 
    for feedback in feedback_list:
     print(i, feedback)
     i += 1

def add_feedback():
    fb = input("Enter feedback: ")
    if fb.strip():
        feedback_list.append(fb)
        print("Added.")
    else:
        print("Invalid input.")

def update_feedback():
    view_feedback()
    try:
        num = int(input("Enter number to update: ")) - 1
        if 0 <= num < len(feedback_list):
            new_fb = input("Enter new feedback: ")
            feedback_list[num] = new_fb
            print("Updated.")
        else:
            print("Invalid number.")
    except:
        print("Enter a valid number.")

def delete_feedback():
    view_feedback()
    try:
        num = int(input("Enter number to delete: ")) - 1
        if 0 <= num < len(feedback_list):
            feedback_list.pop(num)
            print("Deleted.")
        else:
            print("Invalid number.")
    except:
        print("Enter a valid number.")

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Choose 1-5: ")

        if choice == '1':
            view_feedback()
        elif choice == '2':
            add_feedback()
        elif choice == '3':
            update_feedback()
        elif choice == '4':
            delete_feedback()
        elif choice == '5':
            print("Bye!")
            break
        else:
            print("Try again.")
