import sys 
a = int(sys.argv[1]) 

for i in range(0, a):
    result = ' '*(a - i - 1) + '#'*(i + 1)
    print(result)
