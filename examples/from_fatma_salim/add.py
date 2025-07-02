def add_feedback(feedback_list):
    fb = input("Enter feedback: ")
    if fb.strip():
        feedback_list.append(fb)
        print("Added.")
    else:
        print("Invalid input.")

if __name__ == "__main__":
    sample = []
    add_feedback(sample)
    print(sample)