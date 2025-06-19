
import re

def upfb(fblist):
    while True:
        fb = input("Type the ID number of feedback you want to update or 'done' to exit: ")
        if fb == "done":
            break
        fbi = int(fb)
        if fbi < 0 or fbi >= len(fblist):
            print(f"Enter a correct ID number of feedback from 0 to {len(fblist)-1}")
            continue
        print(f"The current feed back: {fblist[fbi]}")
        refb = input("Type your updated feedback here: ")
        if re.match(r"[a-zA-Z0-9]", refb):
            fblist[fbi] = refb
            print("Feedback updated")
        else:
            print("Use alphanumeric characters only")

if __name__ == "__main__":
    lalist = []
    upfb(lalist)