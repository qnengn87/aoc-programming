contents = open("input.txt").read().splitlines()
#contents = ["aaa"]

nice_strings = []

vowels = ["a", "e", "i", "o", "u"]
bad_strings = ["ab", "cd", "pq", "xy"]

def has_vowels(string):
    count = 0
    for v in vowels:
        count += string.count(v)
    if count >= 3:
        return True
    return False
    
def has_bad_string(string):
    for bs in bad_strings:
        if bs in string:
            return True
    return False
    
def has_consecutive_char(string):
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False

for line in contents:
    if not has_bad_string(line):
        if (has_vowels(line) and has_consecutive_char(line)):
            nice_strings.append(line)

print(len(nice_strings))
