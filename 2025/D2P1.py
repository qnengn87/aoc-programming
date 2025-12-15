contents = open("input.txt").read().split(",") # read the contents of the file, splitting them by comma

# for each line, get the first number and the second number (convert them to int)
# for repeating patterns, it needs to be of an even length (2 of the same pattern)
# so filter to even length of the numbers
# split them in half
# if the first half is the same as a second half, store this as an invalid_id
# after all lines, solution is to go through the list and add all the numbers together

invalid_ids = []

for line in contents:
    x, y = line.split("-")
    start, end = int(x), int(y)

    for i in range(start, end+1):
        if len(str(i))%2 != 0: # inverse for readability, less nesting
            continue
        
        num_as_string = str(i)
        length = int(len(num_as_string)/2) # could use floor instead to convert float to int instead of int()
        first_half = num_as_string[:length]
        second_half = num_as_string[length:]
        if first_half == second_half:
            invalid_ids.append(i)

print(sum(invalid_ids))
