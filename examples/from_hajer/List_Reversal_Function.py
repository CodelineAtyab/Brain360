#Implement reversal function list

def reverse_list(list):
    result = []
    item = len(list) - 1
    while item >= 0:
        result.append(list[item])
        item -= 1
    return result

items = input("Enter random items separated by commas: ")
original = items.split(",")
reverse = reverse_list(original)

print("Original list:", original)
print("Reversed list:", reverse)
