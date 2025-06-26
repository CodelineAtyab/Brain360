def clear(feedlist):
    print("\n****(Clear Feedback)****")
    if not feedlist:
        print("The feedback is empty\n")
        return
        
    confirming = input("Are you sure you want to clear all?(yes/no): ").lower()
    if confirming == 'yes':
        feedlist.clear()
        print("Feedback cleared successfully\n")
    else:
        print("Clear cancelled\n")
if __name__ == "__main__":
    test5 = [8, "good"]
    clear(test5)
    print(test5)