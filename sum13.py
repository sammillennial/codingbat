# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6

def sum13(nums):
  ignore = False
  total = 0
  for i in nums:
    if i == 13:
      ignore = True
      continue
    if ignore: # if ignore is turned on, turn it off after going through this step. This
                # skips an item, what we need done. 
      ignore = False
      continue
    total += i
  return total
  
# had i = i+2 but was not working for usable values mixed in after 13

# continue vs. break
