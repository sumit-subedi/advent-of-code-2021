with open("input.txt") as f:
    content = f.read().split("\n")
    lanternfish = [int(i) for i in content[0].split(',')]
    state = [0] * 9
    
    day = 256 # Change this according to day
    
    for i in lanternfish:
        state[i] += 1
    for _ in range(day):
        state0 = state[0]
        for i in range(0, 8): state[i] = state[i+1]
        state[6] += state0
        state[8] = state0
    print(sum(state))

