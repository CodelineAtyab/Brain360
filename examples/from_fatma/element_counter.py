data = []

while True:
    item = input("enter data to the list OR (done) to exit: ")
    if item != "done":
        data.append(item)
    else:
        break
element_to_count = input("enter an element to count: ")

def element_counter(lst,count_element):
    count = 0
    if lst == []:
        print(count)
    else:
        for i in lst:
            if i == count_element:
                count += 1
        print(count)

element_counter(data,element_to_count)