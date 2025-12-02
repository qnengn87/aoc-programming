file = open('input.txt', 'r')
content = file.read()
open_brackets = content.count('(')
close_brackets = content.count(')')
solution = open_brackets - close_brackets
print(solution)
