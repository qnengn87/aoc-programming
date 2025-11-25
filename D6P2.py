import numpy as np 

contents = open("input.txt").read().splitlines()

grid = np.zeros((1000,1000))

def grab_indices(line):
    indices = []
    new_line = line.replace(',', ' ').split()
    for word in new_line:
        if word.isdigit():
            indices.append(int(word))
    indices[2] += 1
    indices[3] += 1
    return indices

# increase light by 1
def turn_on(indices):
    grid[indices[0]:indices[2], indices[1]:indices[3]] += 1

# decrease light by 1, light brightness minimum 0
def turn_off(indices):
    mask = grid[indices[0]:indices[2], indices[1]:indices[3]] > 0
    grid[indices[0]:indices[2], indices[1]:indices[3]][mask] -= 1

# increase light by 2
def toggle(indices):
    grid[indices[0]:indices[2], indices[1]:indices[3]] += 2 
    


for line in contents:
    indices = grab_indices(line)
    if "turn on" in line:
        turn_on(indices)
    elif "turn off" in line:
        turn_off(indices)
    elif "toggle" in line:
        toggle(indices)

print(grid.sum())
