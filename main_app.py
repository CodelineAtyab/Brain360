"""
An Application that takes user feedback as input until the user
Decides to exit.
It also prints all of the statements after user decides to stop giving inputs.
"""

# Declaration

current_feedback = ""
list_of_feedback = []

# Input
while current_feedback != "done":
  current_feedback = input("What's your feedback [type 'done' to exit]: ")
  if current_feedback != "done":
    list_of_feedback.append(current_feedback)

# Process
count = 0
while count < len(list_of_feedback):
  list_of_feedback[count] = "[USER MESSAGE] " + list_of_feedback[count]
  count = count + 1

# Output
count = 0
while count < len(list_of_feedback):
  print(list_of_feedback[count])
  count = count + 1

for item in list_of_feedback:
  print(item)

print(list_of_feedback)

print("EXITING APP")