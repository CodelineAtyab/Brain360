# Declaration and Definition of a function
def say_thanks(f, *args, **kwargs):
  def wrapper():
    f(*args, **kwargs)
    print("Thank You for Calling Sum!!!")
  return wrapper

@say_thanks
def sum(*args, **kwargs):
  result = 0
  for num in args:
    result = result + num
  print(result)
  print(kwargs)


list_of_nums = [1, 3, 6, 4, 5, 6, 9]
d = {"label": "Random Numbers", "toSend": "Some name !!!"}

# sum()
sum(*list_of_nums, **d)
# sum(1, 3, 6)
# sum(2, 6, 7, 3, 4, 56, 78)
# sum(1, 3, 6, 4, 5)
# sum(1, 3, 6, 4, 5, 6, 9, 3, 7, 11, 20)
# sum(1, 3, 6, 4, 5, 6, 9, 3, 7, 11, 20, 21, last_number=100, percentage=10)

# def sum(n1=0, n2=0, n3=0, n4=0, n5=0, n6=0, n7=0, *args):
#   print(n1+n2)
#   print(args)

# sum()
# sum(1, 3, 6, 4, 5, 6, 9)
# sum(1, 3, 6)
# sum(2, 6, 7, 3, 4, 56, 78)
# sum(1, 3, 6, 4, 5)
# sum(1, 3, 6, 4, 5, 6, 9, 3, 7, 11, 20)
# sum(1, 3, 6, 4, 5, 6, 9, 3, 7, 11, 20, 21)

# def greet_the_team(team_name, member_count, name_of_repo, no_of_open_prs, t1, t2):
#   print(f"Welcome Team {team_name} !!!")
#   print(f"Total Team Members are: {member_count}")
#   print(f"Name of GitHub Repo is: {name_of_repo}")
#   print(f"PRs for {name_of_repo} are: {no_of_open_prs}")

#   print("The Team Members Registered are as Follows:")
#   print(t1)
#   print(t2)
#   print("")

# # Calling the function
# greet_the_team(team_name="Brain & Bytes", member_count=23, name_of_repo="Brain360", 
#                no_of_open_prs=106, t1="Quds", t2="Shihab")

# greet_the_team(
#   team_name="Code Orbit", 
#   member_count=22, 
#   name_of_repo="OrbitXO", 
#   no_of_open_prs=23,
#   t1="Mahmood",
#   t2="Adham"
# )



