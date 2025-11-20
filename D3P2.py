file = open('input.txt', 'r')
content = file.read()

x = 0
y = 0
x_robo = 0
y_robo = 0
start_pos = (x,y)
house_visited = set()
house_visited.add(start_pos)
dx = 0
dy = 0

for i, char in enumerate(content):
    match char:
            case '^':
                dx = 1
            case 'v':
                dx = -1
            case '>':
                dy = 1
            case '<':
                dy = -1
    if i%2 == 0:
        x += dx
        y += dy
        curr_pos = (x,y)
    else:
        x_robo += dx
        y_robo += dy
        curr_pos = (x_robo,y_robo)
    house_visited.add(curr_pos)
    dx = 0
    dy = 0 


print(len(house_visited))
    
