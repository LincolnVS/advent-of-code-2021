#read from input.txt
with open('Day 2/input.txt', 'r') as f:
    data = f.read()

#convert data to list of command and units
data = data.split('\n')
data = [l.split() for l in data]

# Part 1
pos_x,depth  = 0,0
for command,unit in data:
    if command == 'forward':
        pos_x += int(unit)
    elif command == 'up':
        depth -= int(unit)
    elif command == 'down':
        depth += int(unit)

print(pos_x*depth)

# Part 2
pos_x,depth,aim  = 0,0,0
for command,unit in data:
    if command == 'forward':
        pos_x += int(unit)
        depth += int(unit)*aim
    elif command == 'up':
        aim -= int(unit)
    elif command == 'down':
        aim += int(unit)

print(pos_x*depth)
