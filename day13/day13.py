from collections import defaultdict
d = defaultdict(int)

with open('input.txt', 'r') as f:
    content = f.readlines()
    i = content.index('\n')
    dots, folds = [i.strip() for i in content[0:i]], [j.strip() for j in content[i+1:]]
    print(folds)
    for i in dots:
        a, b = [int(n) for n in i.split(',')]
        d[a, b] = 1

    def fold(points, axis, coord):
        temp = points.copy()
        if axis == 'y':
            
            for i, j in temp:
                # print(i, j)
                if j == coord:
                    print('here', i, j)
                    del d[i, j]
                if j > coord:
                    # print('here', i, j-((j-coord)*2))
                    del points[i, j] 
                    points[i, 2*coord - j] = 1
                    
        elif axis == 'x':
            for i, j in temp:
                if i == coord:
                    print('here', i, j)
                    del d[i, j]
                if i > coord:
                    # print('here', i-(i-coord)*2, j)
                    del points[i, j]
                    points[2*coord - i, j] = 1
        return points
    
    for i in folds:
        axis, coord = i.split()[-1].split('=')
        temp = fold(d, axis, int(coord))
        
        d = temp.copy()
            
        print(len(d.values()))
    
    i, j = max([i for i,j in d.keys()]), max([j for i, j in d.keys()])

    for x in range(j+1):
        for y in range(i+1):
            if (y, x) in d.keys():
                print('#', end="")
            else:
                print('.', end="")
        print()
