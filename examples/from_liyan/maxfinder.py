import numpy as np
import pandas as pd

# declaration
num = []

#input
while True:
 user_input= (input("write a list of numbers to find the maximum (type 'stop' to viwe): "))
 if user_input == 'stop':
  break
 number = int(user_input)
 num.append(number)

 #processing input 
if num:
    mom = max(num)

print(mom)