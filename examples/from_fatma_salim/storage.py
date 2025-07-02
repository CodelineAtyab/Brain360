import csv
import os

FILE_PATH = "./data/feedback.csv"

def load_feedback():
    feedback = []
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, newline='', mode='r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    feedback.append(row[0])  # Just feedback text
    return feedback

def save_feedback(feedback_list):
    import os
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)  # ← Add this line

    with open(FILE_PATH, mode='w', newline='') as f:
        writer = csv.writer(f)
        for feedback in feedback_list:
            writer.writerow([feedback])
if __name__ == "__main__":
    test_feedback = ["Great session!", "Improve timing."]
    save_feedback(test_feedback)

    loaded = load_feedback()
    print("Loaded feedback:")
    for fb in loaded:
        print("-", fb)

