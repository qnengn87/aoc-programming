contents = open("input.txt").read().splitlines()

wires = {}

def determine_operation(line_as_list):
    line_length = len(line_as_list)
    
    match line_length:
        case 3:
            return "assign"
        case 4:
            return "not"
        case 5:
            operation = line_as_list[1]
            match operation:
                case "AND":
                    return "and"
                case "OR":
                    return "or"
                case "LSHIFT":
                    return "left_shift"
                case "RSHIFT":
                    return "right_shift"
    return False
    
# if source is a digit, return as an integer 
# if source is a a wire, return value of wire source
def get_source_value(source):
    if source.isdigit():
        return int(source)
    else:
        return wires[source]
    
# check which operation, grab the source(s) and target given the type of operation
# get value of source(s) and target, executive operation using bitwise operators
# add/ update target value to dictionary
def execute_operation(operation, line_as_list):
    if operation == "assign":
        source = line_as_list[0]
        target = line_as_list[2]
        
        value = get_source_value(source)
        wires[target] = value
        return
    
    if operation == "not":
        source = line_as_list[1]
        target = line_as_list[3]
        
        value = get_source_value(source)
        wires[target] = ~value
        return 
    
    source_1 = line_as_list[0]
    source_2 = line_as_list[2]
    target = line_as_list[4]
    
    value_1 = get_source_value(source_1)
    value_2 = get_source_value(source_2)
    
    match operation:        
        case "or":
            wires[target] = value_1 | value_2
            return
        
        case "and":
            wires[target] = value_1 & value_2
            return
        
        case "left_shift":
            wires[target] = value_1 << value_2
            return
        
        case "right_shift":
            wires[target] = value_1 >> value_2
    
    return False

# for each line, split the line by space, and determine operation 
# executive operation and store into wire dictionary 
for line in contents:
    line_as_list = line.split()
    operation = determine_operation(line_as_list)
    execute_operation(operation, line_as_list)

print(wires)