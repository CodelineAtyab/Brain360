l = list()
t = tuple()
d = dict()

l = []
t = (0,)
d = {}

# l = ["B&B", 23, "Data Science"]
# d = {"name": "B&B", "members": 23, "topic": "Data Science"}

# Access an Element
# print(d["name"])
# print(d["members"])
# print(d["topic"])
# print(l[0])
# print(l[1])
# print(l[2])

# Add an element to a dict
# d["trainer_name"] = "Atyab"

# # Update
# l[0] = "Brain & Bytes"
# d["name"] = "Brain & Bytes"

# # Access each element one by one
# for item in l:
#   print(item)

# for item in d.items():
#   print(item)

word_dict = {
  "team": "Group of people with a team lead",
  "bottle": "A capped container",
  "pen": "Writing tool with ink",
  "paper": "sheet to write something on"
}

list_of_word_meaning = [
  ["team", "Group of people with a team lead"], 
  ["bottle", "A capped container"], 
  ["pen", "Writing tool with ink"], 
  ["paper", "Sheet to write something on"]
]

print(word_dict["team"])
print(word_dict["pen"])
print(list_of_word_meaning[2][1])