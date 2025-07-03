# Simple feedback system to collect and manage user comments
import json
import os
from datetime import datetime

feedback_file = 'feedback.json'

def load_feedback():
    if not os.path.exists(feedback_file):
        return []
    try:
        with open(feedback_file, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Invalid feedback file format!")
        return []
    except Exception as e:
        print("Error loading feedback:", e)
        return []

def save_feedback(feedback_list):
    try:
        with open(feedback_file, 'w') as f:
            json.dump(feedback_list, f, indent=2)
        return True
    except Exception as e:
        print("Couldn't save feedback:", e)
        return False

def add_feedback(name, message, rating=None):
    all_feedback = load_feedback()
    entry = {
        'id': len(all_feedback) + 1,
        'name': name.strip(),
        'message': message.strip(),
        'date': str(datetime.now().date())
    }

    if rating is not None and 1 <= rating <= 5:
        entry['rating'] = rating

    all_feedback.append(entry)
    save_feedback(all_feedback)
    print("Thanks for sharing your feedback!")
    return entry

def show_all_feedback():
    feedback = load_feedback()

    if not feedback:
        print("There's no feedback yet!")
        return

    print("\nAll feedback:")
    for item in feedback:
        # Skip malformed entries safely
        if not all(k in item for k in ['id', 'name', 'message', 'date']):
            print("⚠️ Skipping invalid entry:", item)
            continue

        print(f"\nID: {item['id']}")
        print(f"From: {item['name']}")
        print(f"Date: {item['date']}")

        if 'rating' in item:
            stars = '*' * item['rating']
            empty = '-' * (5 - item['rating'])
            print(f"Rating: {stars}{empty}")

        print(f"Message: {item['message']}")

    print(f"\nTotal feedback entries: {len(feedback)}")

def remove_feedback(feedback_id):
    all_feedback = load_feedback()
    updated = [fb for fb in all_feedback if fb.get('id') != feedback_id]

    if len(updated) < len(all_feedback):
        save_feedback(updated)
        print(f"Removed feedback #{feedback_id}")
        return True
    else:
        print(f"Feedback #{feedback_id} not found.")
        return False

if __name__ == "__main__":
    print("Welcome to our feedback system!")

    while True:
        print("\nMenu:")
        print("1. Leave feedback")
        print("2. View feedback")
        print("3. Delete feedback")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            name = input("Enter your name: ")
            message = input("Enter your message: ")
            rating = input("Give a rating from 1 to 5 (press Enter to skip): ")

            try:
                rating = int(rating) if rating else None
                if rating is not None and not (1 <= rating <= 5):
                    print("Rating must be between 1 and 5.")
                    rating = None
            except ValueError:
                print("Invalid rating input, skipping rating.")
                rating = None

            add_feedback(name, message, rating)

        elif choice == '2':
            show_all_feedback()

        elif choice == '3':
            try:
                fb_id = int(input("Enter an ID to remove: "))
                remove_feedback(fb_id)
            except ValueError:
                print("Please enter a valid number!")

        elif choice == '4':
            print("Thank you. Goodbye!")
            break

        else:
            print("Please choose a valid option (1–4).")
