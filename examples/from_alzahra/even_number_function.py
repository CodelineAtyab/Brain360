'''As a Python developer, I need a function that processes a list of integers and returns a new list. This new list should only contain the even numbers from the input list, maintaining their original relative order.

Acceptance Criteria:
The function must accept one argument: a list of integers.
The function must return a new list.
The returned list should only contain numbers that are even.
The order of the even numbers in the returned list must be the same as their relative order in the input list.
The original input list must not be modified.
If the input list contains no even numbers, the function should return an empty list.
The function should handle an empty input list gracefully by returning an empty list.

Example Input/Output:
Input: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Function Call: get_even_numbers(numbers)
Output: [2, 4, 6, 8, 10]
numbers after call: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] (unchanged)

Generic Hints:
You'll need to iterate through each number in the input list.
The modulo operator (%) is key: number % 2 == 0 checks if a number is even.
Create an empty list and append even numbers to it as you find them.'''

# Step 1: Create the list to store the numbers that entered by the user
list_x=[]
# Ask for number of elements
element_num=int(input("Enter the numbet of elements in the list : "))

# Get elements from the user
for i in range (element_num):
    number=int(input("Enter a number :"))
    list_x.append(number)

print("Original List : " ,list_x)

# Step 2: Define the function
def get_even_numbers(list_x):
    new_list=[]
    for num in list_x:
        if num%2==0:
            new_list.append(num)
    return new_list #Outside the loop to go through all the integers in the list and print out only the even numbers in a new list
    
# Step 3: Call the function and print result
result=get_even_numbers(list_x)
print(f"The Even Number List : {result}")
