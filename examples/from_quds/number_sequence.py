#Task 3 Number Sequence 
number_sequence = int(input("Enter the number of rows (Positive Value!): "))
if number_sequence > 0:
    for count in range(1,number_sequence + 1):
        for inner_count in range(1,count + 1):
            print(inner_count, end="")
        for inner_count in range(count - 1,0,-1):
                print(inner_count, end="")
        print()
else:
   print("Invalid Input")  

