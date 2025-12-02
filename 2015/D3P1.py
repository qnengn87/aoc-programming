import math

file = open('input.txt', 'r')
content = file.read()

x = 0
y = 0
start_pos = (x,y)
house_visited = set()
house_visited.add(start_pos)

for char in content:
    match char:
        case '^':
            x += 1
        case 'v':
            x -= 1
        case '>':
            y += 1
        case '<':
            y -= 1
    curr_pos = (x,y)
    house_visited.add(curr_pos)


print(len(house_visited))
    
