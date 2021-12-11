import sys
with open ('input.txt', 'r') as f:
    content = [[int(j) for j in i.strip()] for i in f.readlines()]
    flashes = 0
    flashed = []

    def findpoints(i, j):
        allpoints = [[i + 1, j], [i-1, j], [i, j-1], [i, j+1], [i+1, j+1], [i+1, j-1], [i-1, j+1], [i-1, j-1]]
        if i == 0:
            allpoints.remove([i-1, j])
            allpoints.remove([i-1, j+1])
            allpoints.remove( [i-1, j-1])
        if i == len(content) -1 :
            allpoints.remove([i+1, j] )
            allpoints.remove([i+1, j+1])
            allpoints.remove([i+1, j-1])
        if j == 0:
            allpoints.remove([i, j-1] )
            try:
                allpoints.remove( [i+1, j-1])
            except:
                pass
            try:
                allpoints.remove([i-1, j-1])
            except:
                pass
        if j == len(content[0]) -1:
            allpoints.remove([i, j+1] )
            try: 
                allpoints.remove([i-1, j+1])
            except:
                pass

            try : allpoints.remove([i+1, j+1])
            except: pass
        return allpoints

    def flash(i, j):
        global flashed
        global content
        
        points = findpoints(i, j)
        for point in points:
            if content[point[0]] [point[1]] == 0:
                continue
            else:
                content[point[0]][point[1]] += 1
                if content[point[0]] [point[1]] > 9 and [point[0], point[1]] not in flashed:
                    # content[point[0]] [point[1]] = 0
                    flashed.append([point[0], point[1]])
                    # print(content)
                    flash(point[0], point[1])
    
    for step in range(1000):
        flashed = []
        content = [[j+1 for j in i] for i in content]
        for i in range(0, len(content)):
            for j in range(0, len(content[i])):
                # content[i][j] += 1
                if content[i][j] > 9 and [i, j] not in flashed:
                    # content[i][j] = 0
                    flashed.append([i, j])
                    flash(i,j)
        
        for point in flashed:
            content[point[0]][point[1]] = 0
        print(len(flashed))
        if len((flashed)) == 100:
            print(step)
            break
        # print(content)
        flashes += len(flashed)

    print(flashes)