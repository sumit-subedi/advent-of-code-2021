with open ('input.txt', 'r') as f:
    content = [i.strip() for i in f.readlines()]
    errDict = {')': 3, ']': 57, '}': 1197, '>': 25137 }
    incompDict = {')': 1,']': 2, '}': 3 , '>': 4}
    err = []
    points = []
    open = ['(','{', '<', '[']
    close = [')', '}', '>', ']']
    same = {'(':')', '{':'}', '[':']', '<':'>'}
    for line in content:
        stack = []
        point = 0
        for char in line:
            if char in open:
                stack.append(char)
                # print("added", char)
            elif char in close:
                item = stack.pop()
                # print("removed", char)
                if same[item] != char:
                    # print('error', item, char)
                    err.append(char)
                    stack = []
                    break
        for sym in stack[::-1]:
            mirror = same[sym]
            point = point *5
            point += incompDict[mirror]
        points.append(point)
            
    print(err)
    product = 0
    for char in err:
        product += errDict[char]
    print(product)
    points = [i for i in points if i > 0]
    points.sort()
    print(points[int(len(points)/2)])

   