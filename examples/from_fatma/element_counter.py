data = []
n = int(input("Enter the length of list: "))
for item in range(n):
    item = input("enter data to the list: ")
    data.append(item)

element_to_count = input("enter an element to count: ")

def element_counter(data,element_to_count):
    count = 0
    for i in data:
        if i == element_to_count:
            count += 1
    print(count)

element_counter(data,element_to_count)