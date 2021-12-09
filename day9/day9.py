with open('input.txt', 'r') as f:
    content = [[j for j in i.strip()] for i in f.readlines() ]
    contentCopy = content.copy()
    test_dict = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}
    print(content)
    lowest = []

    def getdirection(i, j):
        test = ['up', 'down', 'left', 'right']
            
        if i == 0:
           
            test.remove('up')  #  Delete UP
        elif i == len(content) - 1:
            test.remove('down')  #  Don't check down
        if j == 0:
            test.remove('left')  #  Don't check left
        elif j == len(content[i]) - 1: 
            test.remove('right')  #  Don't check right
        return test

    def get_basin(matrice, i, j):
        if 0 <= i < len(matrice) and 0 <= j < len(matrice[i]) and matrice[i][j] != '9':
            matrice[i][j] = '9'
            return (
                1
                + get_basin(matrice, i - 1, j)
                + get_basin(matrice, i + 1, j)
                + get_basin(matrice, i, j - 1)
                + get_basin(matrice, i, j + 1)
            )
        return 0
            


    
    
    for i in range(0, len(content)):
        for j in range(0, len(content[i])):
            notLowest = True
            test = getdirection(i, j)
            # print(lowest, content[i][j], test)
            for cond in test:
                # print(int(content[i][j]) < int(content[i + test_dict[cond][0]] [j + test_dict[cond][1]]))
                if  int(content[i][j]) < int(content[i + test_dict[cond][0]] [j + test_dict[cond][1]]):
                    continue
                else:
                    notLowest = False
                    break
            if notLowest:
                lowest.append([i, j])
                # tempbasin = findbasin(contentCopy, i, j)
                # print(tempbasin)
                
    
    print(sum([int(content[i][j]) + 1 for i, j in lowest]))
    basin = []
    

    for i, j in lowest:
        basin.append(get_basin(content, i, j))
    basin.sort()
    print(basin)
    print(basin[-1] * basin[-2] * basin[-3])
    