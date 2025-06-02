# Declaration
data_store_file_name = "./reg_users.txt"

list_of_registered_users = [
  {"name": "Mr.Admin", "email": "admin@Bbapp.com"},
  {"name": "Mr.Guest", "email": "guest@Bbapp.com"}
]

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
    fo = open(data_store_file_name, "a")
    fo.write(str({"name": user_name_input, "email": user_email_input}) + "\n")
    fo.close()

  else:
    is_registering_users = False

# Process

# Output
for user_record in list_of_registered_users:
  print(user_record)
