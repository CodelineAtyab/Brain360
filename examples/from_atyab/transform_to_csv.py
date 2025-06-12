# Input
lines_in_file = []
with open("./data/reg_users.txt", "r") as reg_user_file:
  lines_in_file = reg_user_file.readlines()

# Process
data_dicts = []
for line in lines_in_file:
  try:
    data_dicts.append(eval(line.strip()))
  except:
    pass

lines_to_save = []
for data in data_dicts:
  lines_to_save.append(f'{data["name"]},{data["email"]}\n')

for line in lines_to_save:
  print(line)

# Output
with open("./data/reg_users.txt", "w") as reg_user_file:
  for line in lines_to_save:
    reg_user_file.write(line)

