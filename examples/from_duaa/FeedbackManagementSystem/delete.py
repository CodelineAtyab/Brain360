import view
def delete(feedlist):
    if not feedlist:
        print("List is empty\n")
        return
    view.view(feedlist)
    try:
        num = (input("Enter the Feedback number to remove: (use cancel if you change your maind) ")).strip()
        if num.lower() == 'cancel':
            print("Cancelled\n")
            return 
        num = int(num)
        if 1 <= num <= len(feedlist):
            removed = feedlist.pop(num - 1)
            print(f"'{removed}' removed successfully!\n")
        else:
            print("Error\n")
    except ValueError:
        print("Error Enter a valid number\n")

if __name__ == "__main__":
    test4 = [9, "good"]
    delete(test4)
    print(test4)