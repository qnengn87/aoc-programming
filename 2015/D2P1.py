import math

file = open('input.txt', 'r')
content = file.read().splitlines()

total = 0
for line in content:
    dims = line.split('x')
    dims = [int(d) for d in dims] 
    surface_area = 2*((dims[0]*dims[1])+(dims[0]*dims[2])+(dims[1]*dims[2]))
    
    dims.sort()
    extra = dims[0]*dims[1]
    
    total += surface_area + extra

print(total)
    
