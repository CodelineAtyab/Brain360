list_rev=[]

while True:
    x=input("Enter an element : ")
    if x=="done":
        break
    else:
        list_rev.append(x)


def list_of_rev(list_rev):
    new_list=[]
    for i in list_rev[::-1]:
        new_list.append(i)
    return new_list

print("The original list: ",list_rev)
print("The reversal list is : ", list_of_rev(list_rev))