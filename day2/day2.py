with open('input.txt', 'r') as file:
    arr = file.readlines()
    pos = [0,0]
    aim = [0,0,0]
    for line in arr:
        command, num = line.split()
        if command == 'forward':
            pos[0] += int(num)
            aim[1] += aim[2] * int(num)
        elif command == 'down':
            aim[2] += int(num)
            pos[1] += int(num)
        else:
            aim[2] -= int(num)
            pos[1] -= int(num)

    print("Part 1:", pos[0]*pos[1])
    print("Part 2:", pos[0]*aim[1])