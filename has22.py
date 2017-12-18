# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

# has22([1, 2, 2]) → True
# has22([1, 2, 1, 2]) → False
# has22([2, 1, 2]) → False

def has22(nums):
  two = False
  for i in range(len(nums)-1): # again, when using iteration + int, 
                              # decrease range by that int
    if nums[i] == 2 and nums[i+1] == 2:
      two = True
  return two
