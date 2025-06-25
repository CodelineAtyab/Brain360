import json
import os
FeedbackPath = r"C:\Users\DuaaHilal\Desktop\360Brain\Brain360\examples\from_duaa\FeedbackManagementSystem"
FeedBackFile = os.path.join(FeedbackPath, "THEFeedBacks.json")
def load():
    try:
        with open(FeedBackFile , 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  
def save(feedlist):
    with open(FeedBackFile , 'w') as file:
        json.dump(feedlist, file)
if __name__ == "__main__":
    test_data = ["for test1", "test2"]
    save(test_data)
    Ldata = load()
    print("Test load", Ldata)