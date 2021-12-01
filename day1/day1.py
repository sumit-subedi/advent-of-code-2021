with open('input.txt', 'r') as file:
    arr = file.readlines()
    prev = arr[0].strip()
    greater = 0
    for line in arr[1:]:
        if int(line.strip()) > int(prev):
            greater += 1
        prev = line
    print("1st Part:",greater)
    prev = 9999
    greater = 0
    for i in range(0,len(arr)-2):
        sum = int(arr[i]) + int(arr[i+1]) + int(arr[i+2])
        if sum > prev:
            greater += 1
        prev = sum
    print("2nd Part:", greater)