from collections import Counter
with open("input.txt") as f:
    content = f.read().split("\n")
    visited = Counter()
    for line in content:
        start, end = line.split('->')
        start = [int(i) for i in start.split(',')]
        end = [int(i) for i in end.split(',')]

# Part 1
        # if start[0] == end[0] or start[1] == end[1]:
        #     if start[0] == end[0]:
        #         ini = min(start[1], end[1])
        #         fin = max(start[1], end[1])
        #         for i in range(ini, fin+1):
        #             point = [ start[0], i]
                    
        #             visited[str(point)] += 1
        #     else:
        #         ini = min(start[0], end[0])
        #         fin = max(start[0], end[0])
        #         for i in range(ini, fin+1):
        #             point = [i, start[1]]
                    
        #             visited[str(point)] += 1
        # else:
        #     continue

        # Part 2
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        if dx != 0:
            dx = dx // abs(dx)
        if dy != 0:
            dy = dy // abs(dy)
        visited[str([start[0], start[1]])] += 1
        while start[0] != end[0] or start[1] != end[1]:
        
            start[0] += dx
            start[1] += dy
            visited[str([start[0], start[1]])] += 1
    
    
    print( sum([1 for value in visited.values() if value > 1]))
