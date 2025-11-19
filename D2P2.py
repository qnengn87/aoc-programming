import math

file = open('input.txt', 'r')
content = file.read().splitlines()

total = 0
for line in content:
    dims = line.split('x')
    dims = [int(d) for d in dims] 
    dims.sort()
    perimeter = 2*(dims[0]+dims[1])

    extra = dims[0]*dims[1]*dims[2]
    
    total += perimeter + extra

print(total)
    
