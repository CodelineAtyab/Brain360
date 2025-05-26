#delartion
def finding_max_value(num):
    if not num:
        return None  

#processing 
    max_value = num[0]

   
    for value in num[1:]:
        if value > max_value:
            max_value = value

    return max_value

scores = [70, 90, 80, 30, 50]
temperatures = [-1, -8, -10, -2, -3]

maxscore = finding_max_value(scores)
maxtemp = finding_max_value(temperatures)
#print
print("max is: ", maxscore)
print("max is: ", maxtemp)