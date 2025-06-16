
def delfb(fblist):
    while True:
        delfb = input("Type the ID number of the feedback you want to remove or 'done' to exit ")
        if delfb == "done":
            break
        delfbi = int(delfb)
        if delfbi < 0 or delfbi >= len(fblist):
            print(f"Enter a correct ID number of feedback from 0 to {len(fblist)-1}")
            continue
        del fblist[delfbi]
        print("Feedback removed")

if __name__ == "__main__":
    lalist = []
    delfb(lalist)