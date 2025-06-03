# Declaration
# Absolute Path VS Relative Path
data_store_file_name = "./data/reg_users.txt"

# Load Data From File
list_of_registered_users = []
# fo = open(data_store_file_name, "r")
# list_of_lines = fo.readlines()
# for line in list_of_lines:
#   list_of_registered_users.append(eval(line.strip()))
# fo.close()

list_of_lines = []
with open(data_store_file_name, "r") as fo:
  list_of_lines = fo.readlines()

for line in list_of_lines:
  list_of_registered_users.append(eval(line.strip()))

is_registering_users = True

# Input
while is_registering_users:
  user_name_input = input("Enter User Name (done to exit): ")
  
  if user_name_input != "done":
    user_email_input = input("Enter User Email: ")
    list_of_registered_users.append(
      {"name": user_name_input, "email": user_email_input}
    )

    # Store to file
    # fo = open(data_store_file_name, "a")
    # fo.write(str({"name": user_name_input, "email": user_email_input}) + "\n")
    # fo.close()
    with open(data_store_file_name, "a") as fo:
      fo.write(str({"name": user_name_input, "email": user_email_input}) + "\n")
  else:
    is_registering_users = False

# Process

# Output

for user_record in list_of_registered_users:
  print(user_record)
