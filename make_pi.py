# Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.

# make_pi() → [3, 1, 4]

def make_pi():
  x = str(math.pi)
  v = []
  y = int(x[0])
  z = int(x[2])
  w = int(x[3])
  v = [y,z,w]
  return v
