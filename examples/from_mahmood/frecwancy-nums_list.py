list_nums =[]
total=0
nums="0"
while nums !="done":
    nums=input("enter the number that want to added to the list: ")
    if nums!= "done":
        list_nums.append(nums)
print(list_nums)
def count(list_nums, total):
    for i in range(len(list_nums)):
        total+=1
    return total
print("Total items in the list:", count(list_nums, total))
