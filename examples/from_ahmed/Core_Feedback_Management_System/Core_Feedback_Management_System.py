from add_func import addfb
from view_func import viewfb
from update_func import upfb
from delete_func import delfb
import file_operations
fblist = []
data_file = "C:/PyStuff/Brain360/examples/from_ahmed/Core_Feedback_Management_System/Feedback_list.txt"

file_operations.loadfb(data_file)

while True:
    print("Type '1' to show the list of feedbacks")
    print("Type '2' to add a feedback")
    print("Type '3' to update a feedback")
    print("Type '4' to remove a feedback")
    print("Type 'done' to exit the")

    menu = input()
    if menu ==  "1":
        viewfb(fblist)
    if menu == "2":
        addfb(fblist)
    if menu == "3":
        upfb(fblist)
    if menu == "4":
        delfb(fblist)
    if menu == "done":
        break

file_operations.savefb(data_file, fblist)