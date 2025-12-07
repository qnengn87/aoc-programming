import math

contents = open("input-2.txt").read().splitlines()

dial_point = 50
count_pass_zero = 0

# starting dial start point = 50
# left = -1 
# right = +1
# each dial has a distance value

# dial change = (current dial value + (left or right * distance value))
# if the mod of the number is 0, then add to count_at_zero
# get current position by modding with 100 

# day 2 
# if 0 - counts as zero
# if 0 is between the prev number and the current number after the dial change, counts as having gone past 0
# or what is the smallest number change for it to count as zero, if it's greater or equal to that than counts as 0 
## or what is the smallest change of that and get the floored of (smallest/distance) which will tell you how many times it would hit zero 
# 

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
    
    min_distance_left = dial_point
    min_distance_right = 100-dial_point

    # if travelling to the left, distance needs to be larger than the minimum to reach 0
    if distance < 0 and abs(distance) >= min_distance_left:
        if dial_point == 0 and (abs(distance) < 100):
            pass
        else:
            # something wrong here?
            count_pass_zero += (abs(distance//100)) # distance because looking at rotations, otherwise you lose from the minus
    
    if distance > 0 and abs(distance) >= min_distance_right:
        if dial_point == 0 and (abs(distance) < 100):
            pass
        else:
            if new_position%100 == 0  and dial_point != 0:
                count_pass_zero += 1
            else:
                count_pass_zero += (abs((new_position//100))) # new position because rotations
    
    # if new_position == 0 and dial_point != 0:
    #     count_pass_zero += 1
    
    
    #count_pass_zero += (abs(new_position//100))
    
    print(line, dial_point, new_position, distance, min_distance_left, min_distance_right, (new_position%100), count_pass_zero)
    
    dial_point = new_position%100
    
    # print(dial_point)

print(count_pass_zero)


