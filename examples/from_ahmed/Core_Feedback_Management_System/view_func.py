
def viewfb(fblist):
    while True:
        print("List of feedbacks: ")
        for fbnum in range(len(fblist)):
            print(f"ID: {fbnum} . Feedback: {fblist[fbnum]}")
        exit = input("Type 'done' to exit ")
        print()
        if exit == "done":
            break

if __name__ == "__main__":
    lalist = []
    viewfb(lalist)