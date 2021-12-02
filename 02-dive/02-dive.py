file = open('02-dive-input.txt', 'r')
commands = [(
        c.strip().split(" ")[0],
        int(c.strip().split(" ")[1])
    ) for c in file.readlines()
]

depth, forward = 0, 0
for command in commands:
    if command[0] == 'forward':
        forward += command[1]
    else:
        depth += (command[1] if command[0] == 'down' else -command[1])
print(depth * forward)

depth, forward, aim = 0, 0, 0
for command in commands:
    if command[0] == 'forward':
        forward += command[1]
        depth += command[1] * aim
    else:
        aim += (command[1] if command[0] == 'down' else -command[1])

print(depth * forward)