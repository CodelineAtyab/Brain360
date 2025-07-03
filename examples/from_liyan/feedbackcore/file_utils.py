import json
import os

JSON_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "feedback.json")

def load_feedback(path=JSON_PATH):
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_feedback(data, path=JSON_PATH):
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        print(f">>> Feedback saved to {path}")
    except Exception as e:
        print(f"Error saving feedback: {e}")

