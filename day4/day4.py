with open("input.txt") as f:
    content = f.read().split("\n")[:~0]
    nums = [int(x) for x in content[0].split(",")]
    bingo = content[2:]
new_bingo = [[]]
i = 0
for row in bingo:
    if row == "":
        new_bingo.append([])
        i+=1
    else:
        try:
            row = list(eval(row.replace(" ",",").replace(",,",",")))
        except:
            row = list(eval(row.replace(" ",",").replace(",,",",")[1:]))
        new_bingo[i].append(row)
bingo = new_bingo
wins = [[]]
for i in range(len(bingo)):
    cols = [[],[],[],[],[]]
    for row in bingo[i]:
        for j in range(len(row)):
            cols[j].append(row[j])
        wins[i].append(row)
    for col in cols:
        wins[i].append(col)
    wins.append([])

def check():
    lst = []
    for num in nums:
        lst.append(num)
        for board in wins:
            for win in board:
                if all(x in lst for x in win):
                    return [lst,board]

def last():
    lst = []
    won = []
    for num in nums:
        if len(won) != len(bingo):
            lst.append(num)
        for board in wins:
            for win in board:
                if all(x in lst for x in win) and board not in won:
                    won.append(board)
    return [lst,won[~0]]


board = check()
s = 0
for row in board[1]:
    for num in row:
        if num not in board[0]:
            s += num
last_one = last()
l = 0
for row in last_one[1]:
    for num in row:
        if num not in last_one[0]:
            l += num

answer_one = str(s * board[0][~0]//2)
answer_two = str(l * last_one[0][~0]//2)
print("p1: " + answer_one)
print("p2: " + answer_two)