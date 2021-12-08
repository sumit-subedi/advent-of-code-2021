with open("input.txt") as f:
    output = [[i.split('|')[0].split(), i.split('|')[1].split()] for i in f.readlines() ]
    num_list = ['']*10
    print(num_list)
 
    occur = 0
    total = 0
    for i in output:
        num = 0
        for j in i[1]:
            
            if (len(j) in [2,3,4,7]) :
                
                occur += 1

    def intercept(a, b):
        return len(set(a).intersection(set(b)))

    for i in output:
        for j in 2 * i[0]:
            number = ""
            if len(j) == 2:
                num_list[1] = j
            elif len(j) == 3:
                num_list[7] = j
            elif len(j) == 4:
                num_list[4] = j
            elif len(j) == 7:
                num_list[8] = j
            elif len(j) == 6 and intercept(j, num_list[7]) == 2:
                num_list[6] = j
            elif len(j) == 6 and intercept(j, num_list[4]) == 4:
                num_list[9] = j
            elif len(j) == 6 and intercept(j, num_list[7]) == 3 and intercept(j, num_list[4]) == 3:
                num_list[0] = j
            elif len(j) == 5 and intercept(j, num_list[7]) == 3:
                num_list[3] = j
            elif len(j) == 5 and intercept(j, num_list[4]) == 3 and intercept(j, num_list[7]) == 2:
                num_list[5] = j
            elif len(j) == 5 and intercept(j, num_list[7]) == 2 and intercept(j, num_list[4]) == 2:
                num_list[2] = j
            
         
        for j in i[1]:
            number += [str(i) for i in range(len(num_list)) if set(j) == set(num_list[i])][0]
        total += int(number)
    
   
            
    
    print("Part One:", occur)
    print("Part Two:", total)
