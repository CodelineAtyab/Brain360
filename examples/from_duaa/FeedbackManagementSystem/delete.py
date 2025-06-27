import view
def delete(feedlist):
    if not feedlist:
        print("List is empty\n")
        return
    view.view(feedlist)
    try:
        num = int(input("Enter the Feedback number to remove: "))
        if 1 <= num <= len(feedlist):
            removed = feedlist.pop(num - 1)
            print(f"'{removed}' removed successfully!\n")
        else:
            print("Error\n")
    except ValueError:
        print("Error\n")

if __name__ == "__main__":
    test4 = [9, "good"]
    delete(test4)
    print(test4)