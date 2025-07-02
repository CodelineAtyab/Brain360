def load_feedback(filepath):
    feedbacks = []
    try:
        with open(filepath, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    feedbacks.append(line)
        print(f"Loaded {len(feedbacks)} feedback entries.")
    except FileNotFoundError:
        print("Feedback File Not Found! Starting with empty list.")
    return feedbacks

def save_feedback(filepath, entries):
    try:
        with open(filepath, "w") as file:
            for item in entries:
                file.write(item + "\n")
        print("Feedback Saved to File.")
    except Exception as e:
        print(f"Error Saving File: {e}")

if __name__ == "__main__":
    path = "sample.txt"
    test_data = ["A", "B"]
    save_feedback(path, test_data)
    print(load_feedback(path))