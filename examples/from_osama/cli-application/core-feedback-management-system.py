import add
import feedbackdatabase

print("Welcome to the Feedback Application")

if len(feedbackdatabase.database) == 0:
    print("Your feedback list is empty please add any feedback :(")
    inputted_value = str(input("Please enter a feedback: "))
    if inputted_value != None:
        add(inputted_value)
    else:
        inputted_value = str(input("Please enter a feedback: "))