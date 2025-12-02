import numpy as np 

contents = open("input.txt").read().splitlines()

grid = np.full((1000,1000), False)

def grab_indices(line):
    indices = []
    new_line = line.replace(',', ' ').split()
    for word in new_line:
        if word.isdigit():
            indices.append(int(word))
    # print(indices)
    indices[2] += 1
    indices[3] += 1
    return indices

def turn_on(indices):
    grid[indices[0]:indices[2], indices[1]:indices[3]] = True

def turn_off(indices):
    grid[indices[0]:indices[2], indices[1]:indices[3]] = False

def toggle(indices):
    grid[indices[0]:indices[2], indices[1]:indices[3]] = np.invert(grid[indices[0]:indices[2], indices[1]:indices[3]])
    


for line in contents:
    indices = grab_indices(line)
    if "turn on" in line:
        turn_on(indices)
    elif "turn off" in line:
        turn_off(indices)
    elif "toggle" in line:
        toggle(indices)

print(grid.sum())
