# FUNCTIONS
def sum_list_elements(data_points):
    list_sum.append(data_points)
    print(list_sum)
    return sum(data_points)

def sum_list_elements_empty(empty_list):
    if not empty_list:
        return 0

# DECLARATION
list_sum = []
empty_list = []

# USER INPUT
data_points = list(map(float, input("Enter numbers separated by space: ").split()))

# FUNCTION CALL
if not data_points:
    print("Output:", sum_list_elements_empty(empty_list))
else:
    print("Output:",sum_list_elements(data_points))
