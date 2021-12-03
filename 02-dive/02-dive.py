file = open('02-dive-input.txt', 'r')
commands = [(
        c.strip().split(" ")[0],
        int(c.strip().split(" ")[1])
    ) for c in file.readlines()
]

depth, forward = 0, 0
for (c, n) in commands:
    if c == 'forward':
        forward += n
    else:
        depth += (n if c == 'down' else -n)
print(depth * forward)

depth, forward, aim = 0, 0, 0
for (c, n) in commands:
    if c == 'forward':
        forward += n
        depth += n * aim
    else:
        aim += (n if c == 'down' else -n)

print(depth * forward)