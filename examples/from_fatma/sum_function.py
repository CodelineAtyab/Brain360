list1 = []

while True:
        data = input("Enter a number or (done) to exit: ")
        if data != "done":
            list1.append(float(data))
        else:
            print("List:",list1)
            break

def sum_of_list(lst):
    total = 0
    for n in lst:
        total += n
    print(total)
    return total

sum_of_list(list1)