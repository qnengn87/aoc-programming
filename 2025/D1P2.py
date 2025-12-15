import math

contents = open("input.txt").read().splitlines()

dial_point = 50
count_pass_zero = 0

def get_distance(line):
    distance = int(line[1:])
    if line[0] == "L":
        distance *= -1
    
    return distance

def change_dial(line, point):
    distance = get_distance(line)
    new_position = (point+distance)

    return new_position, distance

for line in contents:
    new_position, distance = change_dial(line, dial_point)

    # travelling to the right
    if distance > 0:
        count_pass_zero += new_position//100

    # travelling to the left
    if distance < 0:
        if dial_point == 0:
            min_distance_to_hit_zero = 100 #distance needs to be 100 if it starts at 0 to be considered a click, otherwise minimum distance is only 0 which is wrong
        else:
            min_distance_to_hit_zero = dial_point
        # if dial has been turned enough to reach zero 
        if abs(distance) >= min_distance_to_hit_zero:
            count_pass_zero += 1
        # now take only the distance from the minimum point to see how much more it has travelled, i.e. any more rotations
            new_distance = abs(distance) - min_distance_to_hit_zero
            count_pass_zero += new_distance//100
            
    
    print(line, dial_point, distance, (new_position%100), count_pass_zero)
    
    dial_point = new_position%100

print(count_pass_zero)


