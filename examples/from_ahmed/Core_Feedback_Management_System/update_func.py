
import re

def upfb(fblist):
    while True:
        fb = input("Type the ID number of feedback you want to update or 'done' to exit: ")
        if fb == "done":
            break
        fbi = int(fb)
        if fbi < 0 or fbi >= len(fblist):
            print("Enter a correct ID bumber of feedback")
            continue
        refb = input("Type your updated feedback here: ")
        if re.match(r"[a-zA-Z0-9]", refb):
            fblist[fbi] = refb
            print("Feedback updated")
        else:
            print("Use alphanumeric characters only")

if __name__ == "__main__":
    lalist = []
    upfb(lalist)