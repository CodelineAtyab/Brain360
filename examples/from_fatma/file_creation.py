import json
import os

file_path = "feedbacks.json"

def load_feedback():
    print("Loading feedback data from file...")
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        data = json.load(file)
        print(f"Found {len(data)} existing feedback entries.")
        return data

def save_feedback(data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)
    print("Feedback saved to file.")