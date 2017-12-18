# Given a string, return a string where for every char in the original, there are two chars.

# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'

def double_char(str):
  new_str = ''
  for i in range(len(str)):
    new_str = new_str + str[i]+str[i]
  return new_str
