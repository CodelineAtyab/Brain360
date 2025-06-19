
import re

def addfb(fblist):
    while True:
        fb = input("Provide your feeddback here or type 'done' to exit: ")
        if fb == "done":
            break
        if re.match(r"[a-zA-Z0-9]", fb):
            fblist.append(fb)
            print("Feedback added")
        else:
            print("Use alphanumeric characters only")

if __name__ == "__main__":
    lalist = []
    addfb(lalist)