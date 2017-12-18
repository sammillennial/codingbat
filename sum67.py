# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

# sum67([1, 2, 2]) → 5
# sum67([1, 2, 2, 6, 99, 99, 7]) → 5
# sum67([1, 1, 6, 7, 2]) → 4

def sum67(nums):
  # so this boolean variable will be like the switch for whether we're reading this
  # item into the count or not
  ignore = False
  total = 0
  
  for i in nums:
      if i == 6:
        ignore = True
        continue
      if i == 7 and ignore: # if we hit a 7 and counting is turned off...
        ignore = False # turn it off
        continue
      if not ignore:
        total += i
  return total
  
  # Didn't work with 6's and 7's out of order and multiple
  # for i in nums:
  # if i == 6:
  #    x = nums.index(6)
  #    y = nums.index(7)
  #    del nums[x:y+1]
  #return sum(nums)
