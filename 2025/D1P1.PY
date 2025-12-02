import re

contents = open("input.txt").read().splitlines()

dial_point = 50
count_at_zero = 0

# starting dial start point = 50
# left = -1 
# right = +1
# each dial has a distance value

# dial change = (current dial value + (left or right * distance value))
# if the mod of the number is 0, then add to count_at_zero
# get current position by modding with 100 


def get_values(line):
    match line[0]:
        case "L":
            direction = "left"
        case "R":
            direction = "right"

    distance = re.findall('\d+',line)

    return (direction, int(distance[0]))

def change_dial(line):
    values = get_values(line)
    match values[0]:
        case 'left':
            change = dial_point+(-1*values[1])
        case right:
            change = dial_point+(values[1])

    dial_change = change%100
    
    return dial_change

for line in contents:
    dial_change = change_dial(line)
    if dial_change == 0:
        count_at_zero += 1
    dial_point = dial_change

print(count_at_zero)


