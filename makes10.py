# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

# makes10(9, 10) → True
# makes10(9, 9) → False
# makes10(1, 9) → True

def makes10(a, b):
  x = False;
  if a==10 or b==10:
    x = True
  elif abs(a+b)==10:
    x = True
  else: False
  return x;
