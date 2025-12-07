contents = open("input.txt").read().splitlines()

dial_point = 50
count_at_zero = 0

def get_distance(line):
    distance = int(line[1:])
    if line[0] == "L":
        distance *= -1
    
    return distance

def change_dial(line, point):
    distance = get_distance(line)
    change = (point+distance)%100

    return change

for line in contents:
    dial_point = change_dial(line, dial_point)
    count_at_zero += (dial_point == 0)

print(count_at_zero)


