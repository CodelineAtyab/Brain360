import json
import os
import re

feedback_list = []

def load_data():
    print("\nanonymous feedback system")
    print("loading your feedback...")
    try:
        if os.path.exists('feedback.json'):
            with open('feedback.json', 'r') as f:
                feedback_list.extend(json.load(f))
            print(f"found {len(feedback_list)} saved feedback items\n")
        else:
            print("no saved feedback yet\n")
    except:
        print("can't load saved feedback!\n")

def save_data():
    try:
        with open('feedback.json', 'w') as f:
            json.dump(feedback_list, f)
        print("feedback saved\n")
    except:
        print("couldn't save feedback\n")

def is_valid(text):
    if not text.strip():
        print("feedback can't be empty")
        return False
    if not re.match("^[a-z0-9 ]+$", text.lower()):
        print("only letters, numbers and spaces allowed")
        return False
    return True

def add_feedback():
    while True:
        text = input("enter your feedback: ")
        if is_valid(text):
            feedback_list.append({
                'id': len(feedback_list)+1,
                'text': text
            })
            print("added successfully!")
            save_data()
            return

def update_feedback():
    if not feedback_list:
        print("nothing to update\n")
        return
        
    while True:
        try:
            item_id = int(input("enter id to update: "))
            if 1 <= item_id <= len(feedback_list):
                item = feedback_list[item_id-1]
                print(f"\ncurrent: {item['text']}")
                new_text = input("enter new text: ")
                if is_valid(new_text):
                    item['text'] = new_text
                    print("updated successfully!")
                    save_data()
                    return
            else:
                print(f"please enter 1-{len(feedback_list)}")
        except:
            print("please enter a number")

def delete_feedback():
    if not feedback_list:
        print("nothing to delete\n")
        return
        
    while True:
        try:
            item_id = int(input("enter id to delete: "))
            if 1 <= item_id <= len(feedback_list):
                feedback_list.pop(item_id-1)
                print("deleted successfully!")
                save_data()
                return
            else:
                print(f"please enter 1-{len(feedback_list)}")
        except:
            print("please enter a number")

def show_feedback():
    if not feedback_list:
        print("no feedback yet\n")
        return
        
    print("\nall feedback:")
    for item in feedback_list:
        print(f"{item['id']}. {item['text']}")
    print(f"\ntotal: {len(feedback_list)} items\n")

def main():
    load_data()
    
    while True:
        print("menu ")
        print("1. view feedback")
        print("2. add feedback")
        print("3. update feedback")
        print("4. delete feedback")
        print("5. exit")
        
        choice = input("choose an option: ")
        
        if choice == '1':
            show_feedback()
        elif choice == '2':
            add_feedback()
        elif choice == '3':
            update_feedback()
        elif choice == '4':
            delete_feedback()
        elif choice == '5':
            save_data()
            print("\ngoodbye! your feedback is saved.")
            break
        else:
            print("choosean option:\n")

if __name__ == "__main__":
    main()
