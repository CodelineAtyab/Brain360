
'''
while True:
    enter_username =input("Enter Desired Username: ").lower()
    if len(enter_username)<5:
        print(f"Username {enter_username} is too short. It must be at least 5 characters❌")
    elif len(enter_username)>=5:
        print(f"Username {enter_username} is valid")
    elif len(enter_username)>15:
        print(f"Username {enter_username} is too long. It must be no more than 15 characters❗")


def not_string(str):
  if str [0:3] != "not":
    return ( "not" + " " + (str))
  else:
    return(str)
text= input(" enter somthing: ")
print(not_string(text))
'''
def first_half(str):
  result =len(str)//2
  return text[:result]

text=input("Enter word: ")
print(first_half(text))