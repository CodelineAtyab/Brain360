feedback_list = []

while True:
    print("\n  The feedback options")
    print("1. To show feedback")
    print("2. To add feedback")
    print("3. To update feedback")
    print("4. To delete feedback")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        if not feedback_list:
            print("There is no feedback yet!")
        else:
            print("Feedback list:")
            count = 1
            for feedback in feedback_list:
                print(str(count) + ". " + feedback)
                count += 1

    elif choice == "2":
        feedback = input("What is your feedback? ").strip()
        if feedback == "":
            print("You didn't write anything!")
        else:
            feedback_list.append(feedback)
            print("Thank you, your feedback is added!")

    elif choice == "3":
        if not feedback_list:
            print("Nothing to update!")
        else:
            print("Feedback list:")
            count = 1
            for feedback in feedback_list:
                print(str(count) + ". " + feedback)
                count = count + 1

            try:
                number = int(input("Choose a number to update: "))
                if 1 <= number <= len(feedback_list):
                    new_feedback = input("Write new feedback: ").strip()
                    if new_feedback != "":
                        feedback_list[number - 1] = new_feedback
                        print("Your feedback is updated!")
                    else:
                        print("You can't leave this part empty!")
                else:
                    print("You chose an invalid option!")
            except:
                print("Please enter a valid option.")

    elif choice == "4":
        if not feedback_list:
            print("Nothing to delete!")
        else:
            count = 1
            for feedback in feedback_list:
                print(str(count) + ". " + feedback)
                count = count + 1

            try:
                number = int(input("Which number do you want to delete? "))
                if 1 <= number <= len(feedback_list):
                    feedback_list.pop(number - 1)
                    print("Feedback deleted!")
                else:
                    print("You entered an invalid option!")
            except:
                print("Please enter a valid option!")

    elif choice == "5":
        print("Thank you, goodbye!")
        break
    else:
        print("Please choose a valid option!")