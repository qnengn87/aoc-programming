contents = open("input.txt").read().splitlines()
#contents = ["aaa"]

num_nice_strings = 0

def has_pair(string):
    if len(string) < 4:
        return False
    for i in range(len(string)-1):
        pair = string[i] + string[i+1] #string[i:i+2]
        pair_end_index = i+2
        if pair in string[pair_end_index:]:
            return True
    return False

def has_after_next(string):
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False


for line in contents:
    if has_pair(line) and has_after_next(line):
        num_nice_strings += 1

print(num_nice_strings)
