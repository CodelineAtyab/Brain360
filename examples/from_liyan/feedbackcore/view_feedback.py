from file_utils import load_feedback

from file_utils import load_feedback

def view_feedback(_):
    feedbacks = load_feedback()

    if feedbacks:
        print("\nHere it is---------:")
        for i, fb in enumerate(feedbacks, 1):
            print(f"{i}. {fb}")
    else:
        print("\nNo feedback found.")