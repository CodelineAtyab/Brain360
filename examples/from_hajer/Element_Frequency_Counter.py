#Create Element Frequency Counter Function

def count_item(list_items, item_name):
    times = 0
    for name in list_items:
        if name == item_name:
            times = times + 1
    return times

text = input("Enter some items separated by commas: ")
items = text.split(",")
name = input("Enter the item you want to count: ")

answer = count_item(items, name)
print("It appears", answer, "time(s).")

