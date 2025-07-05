def make_chocolate(small, big, goal):
  total=(goal//5)*5
  # print(min(goal//5,big))
  # print(total)
  reminder=goal-total
  if reminder<=small:
    return reminder
  else:
    return -1
print( make_chocolate(6, 2, 7))
print( make_chocolate(3, 1, 9))



