list_rev=[]


def list_of_rev(lis_rev):

    while True:
        x=input("Enter an element : ")
        if x=="done":
            break
        else:
            list_rev.append(x)
    new_list=[]
    for i in list_rev[::-1]:
        new_list.append(i)
    return new_list 

list_of_rev(list_rev)