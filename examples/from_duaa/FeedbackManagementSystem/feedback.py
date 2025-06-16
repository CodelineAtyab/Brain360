import add
import view
import update
import delete
import clear
feedbackList = []
print("Welcome Feedback Management System:)!")
running = True
while running:
    print("\n@@@@@@@@@")
    print("1. Add Feedback")
    print("2. View Feedback")
    print("3. Delete Feedback")
    print("4. Update Feedback")
    print("5. Clear list")
    print("6. Exit")
    print("@@@@@@@@@")
    choice = input("Choose an option: ")
    if choice == "1":
        add.add(feedbackList)
    elif choice == "2":
        view.view(feedbackList)
    elif choice == "3":
        delete.delete(feedbackList)
    elif choice == "4":
        update.update(feedbackList)
    elif choice == "5":
        clear.clear(feedbackList)
    elif choice == "6":
        print("Thank you for using our system! :)")
        running = False
    else:
        print("Invalid choice\n")