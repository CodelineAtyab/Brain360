import re
def add(feedlist):
    print("Add Feedback <3")
    userFeedback = input("How do you feel? Give us your feedback: ").strip()
    
    if not userFeedback:
        print("Error you should input somthing\n")
        return False
        
    if re.search(r"[^\w ]", userFeedback):  
        print("Error just nums and letters\n")
        return False
        
    feedlist.append(userFeedback)
    print(f"\n Your feedback! '{userFeedback}' has been added\n")
    return True

if __name__ == "__main__":
    test1 = []
    add(test1)
    print(test1)