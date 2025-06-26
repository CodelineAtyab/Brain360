import json
import os
FeedbackPath = r"C:\Users\DuaaHilal\Desktop\360Brain\Brain360\examples\from_duaa\FeedbackManagementSystem"
FeedBackFile = os.path.join(FeedbackPath, "THEFeedBacks.json")

def load():
    try:
        with open(FeedBackFile, 'r') as file:
            data = json.load(file)
            print(f"Successfully The Feedback Entries : {len(data)} ")
            return data
    except FileNotFoundError:
        print("No existing feedbacks")
        return []
    except json.JSONDecodeError:
        print("Warning The Feedback file is corrupted ")
        return []
    except PermissionError:
        print("Permission denied")
        return []

def save(feedlist):
    print("Saving :)")
    try:
        with open(FeedBackFile, 'w') as file:
            json.dump(feedlist, file)
        print("Saved successfully")
    except PermissionError:
        print("Permission denied")
    except Exception as exc:
        print(f"Error saving feedback: {str(exc)}")

if __name__ == "__main__":
    test_data = ["for test1", "test2"]
    save(test_data)
    Ldata = load()
    print("Test load", Ldata)