def view(feedlist):
    if not feedlist:
        print("List is empty.\n")
    else:
        print("Feedback List:")
        for i, item in enumerate(feedlist, 1):
            print(f"{i}. {item}")
        print()

if __name__ == "__main__":
    test2 = [8, "good"]
    view(test2)