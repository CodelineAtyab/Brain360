# Create Element Frequency Counter Function
my_data = []
element_to_count = ""
while True:
        data = input("Enter a list of alphabitics and Done when you finish ")
        if data.lower() == "done":
           break
        my_data.append(data)
        print(my_data)

def count_element_occurrences(Numbers,element):
    count = 0 
    for element in Numbers:
       if element == "a":
        count = count + 1 
    return  count
print("Total a is",count_element_occurrences(my_data,element_to_count))

    
