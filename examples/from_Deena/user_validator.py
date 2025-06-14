username = input("Enter your desired username: ")
if len(username) < 5:
    print (f'username "{username}" is too short. It must be at least 5 characters.')
elif len(username) > 15:
    print (f'username "{username}" is too long. It must be no more than 15 characters.')
else:
    print (f'username "{username}" is valid!')