import sys
with open("input.txt") as f:
    content = [int(i) for i in f.read().split(",")]
    max = max(content)
    min = min(content)
    

    least = sys.maxsize
    for i in range(min, max):
        sum = 0
        for j in content:
            # Part One
            # sum += abs(i-j)

            # Part Two
            sum += (abs(i - j)* (abs(i - j) + 1))/2

        
        if sum < least:
            least = sum
    print(least)