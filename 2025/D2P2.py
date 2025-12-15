from textwrap import wrap
from math import sqrt, floor

contents = open("input.txt").read().split(",") # read the contents of the file, splitting them by comma

# for each of the line, you want to know the length of the line
# and check chunk sizes of the factors of the length of the line
# if there are at least 2 consecutive chunks that are the same
# this is considered an invalid id
# add to list and sum up for solution


invalid_ids = set()

def is_invalid(i):
    length = len(str(i))
    for j in range(1, floor(sqrt(length))+1):
        if length%j != 0:
            continue
        for factor in [j, length//j]:
            chunks = wrap(str(i), factor)
            if len(chunks) == 1:
                continue
            if len(set(chunks)) == 1:
                return True
    return False

for line in contents:
    x, y = line.split("-")
    start, end = int(x), int(y)

    for i in range(start, end+1):
        if is_invalid(i):
            invalid_ids.add(i)
        

print(sum(invalid_ids))
