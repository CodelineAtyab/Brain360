from add_func import addfb
from view_func import viewfb
from update_func import upfb
from delete_func import delfb
fblist = []


while True:
    print("Type '1' to add a feedback")
    print("Type '2' to show the list of feedbacks")
    print("Type '3' to update a feedback")
    print("Type '4' to remove a feedback")
    print("Type 'done' to exit the")

    menu = input()
    if menu ==  "1":
        addfb(fblist)
    if menu == "2":
        viewfb(fblist)
    if menu == "3":
        upfb(fblist)
    if menu == "4":
        delfb(fblist)
    if menu == "done":
        break