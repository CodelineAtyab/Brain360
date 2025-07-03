def no_teen_sum(a, b, c):
  teen = [13, 14, 17, 18, 19]
  if a in teen:
    a = 0
  if b in teen:
    b = 0
  if c in teen:
    c = 0

  return a + b + c