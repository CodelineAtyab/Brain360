import store_feedback

def view():
    entries = store_feedback.get_all_feedback()
    if not entries:
        print("No feedback available.")
    else:
        print("All Feedback:")
        for i, entry in enumerate(entries, start=1):
            print(f"{i}. {entry}")

if __name__=="__main__":
    view()
