# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True

def xyz_there(str):
  str = str.replace('.xyz','')
  xyz = 'xyz'
  return xyz in str
  
  #kept solving everything except .xyzxyz. Redo. Replace/remove all .xyz's.
  #if xyz is in there, then solved. 
