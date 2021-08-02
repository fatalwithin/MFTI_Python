import sys 
a = int(sys.argv[1]) 
b = int(sys.argv[2]) 
c = int(sys.argv[3])

d = (b ** 2) - 4*a*c

roots = []

if (d > 0):
  root1 = (-b + d ** 0.5) / (2 * a)
  root2 = (-b - d ** 0.5) / (2 * a)
  roots.append(int(root1))
  roots.append(int(root2))
elif (d == 0):
  root = -b / (2 * a)
  roots.append(int(root))
else:
  pass

for root in roots:
  print(root)