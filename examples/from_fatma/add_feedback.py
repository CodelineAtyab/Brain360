import re
import store_feedback

def add():
    while True:
        data = input("Enter your feedback: ")

        if re.match("^[a-zA-Z0-9 ]+$", data):
            store_feedback.add_feedback(data)
            print("Feedback added successfully!")
            break
        else:
            print("Error: Feedback can only contain alphanumeric characters and spaces.")

if __name__=="__main__":
    add()