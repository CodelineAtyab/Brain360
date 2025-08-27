import re
def add(feedlist):
    userFeedback = input("How do you feel? Give us your feedback: ").strip()
    if not userFeedback:
        print("Error you should input somthing\n")
        return
    if re.search(r"[^\w ]", userFeedback):  
        print("Error just nums and letters\n")
    else:
        feedlist.append(userFeedback)
        print(f"'{userFeedback}' added successfully!:)\n")

if __name__ == "__main__":
    test1 = []
    add(test1)
    print( test1)