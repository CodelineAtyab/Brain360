# weekdays = ("Sun", "Mon", "Tue", "Wed", "Thu")  # Immutable
# team_members = ["Mr.A", "Mr.B", "Ms.C"]  # Mutable

# weekdays[0] = "Super Sun"
# print(team_members)
# print(weekdays)
# print(keyboard_test_text)

def is_the_word_palindrome(word):
  return word.lower() == word.lower()[::-1]


keyboard_test_text = "The Quick BrOwn fox jumps over a lAzy dog."  # Immutable
title = "madam"  # Palindrome String
med_condition = "Aibohphobia"


if is_the_word_palindrome(title):
  print("Its Palindrome Word!")
else:
  print("Not Palindrome")


# for curr_char in keyboard_test_text.lower():
#   # if curr_char == "a" or curr_char == "e" or curr_char == "i" or curr_char == "o" or curr_char == "u":
#   #   print("Vowel Found: ", curr_char)
#   if curr_char in ("a", "e", "i", "o", "u"):
#     print("Vowel Found: ", curr_char)

# print(keyboard_test_text.lower())

# print(keyboard_test_text[8])
# print(keyboard_test_text[::-1])