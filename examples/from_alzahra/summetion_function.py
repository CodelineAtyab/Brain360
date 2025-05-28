# Step 1: Create the list to store the numbers that entered by the user
data_points=[]
# Ask for number of elements
element_num=int(input("Enter the numbet of elements in the list : "))

# Get elements from the user
for i in range (element_num):
    number=float(input("Enter a number :"))
    data_points.append(number)
print(data_points)

# Step 2: Define the function
def sum_list_elements(data_points):
    count=0
    for num in data_points:
        count+=num
    
    return count
# Step 3: Call the function and print result
result=sum_list_elements(data_points)
print(f"{result} is the result !")
