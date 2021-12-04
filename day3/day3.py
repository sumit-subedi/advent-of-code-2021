with open('input.txt', 'r') as file:
    arr = file.readlines()
    most = [[0,0] for _ in range(12)]
    for i in arr:
        for index in range(0, len(i.strip())):
            if int(i[index]) == 0:
                 most[index][0] += 1
            else:
                most[index][1] += 1
    gamma_rate = ""
    epsilon_rate = ""
    for i in range(12):
        if most[i][0] > most[i][1]:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"
    print("Part 1 :", int(gamma_rate, 2) * int(epsilon_rate ,2))

    new_arr_ox = [i for i in arr if i[0] == gamma_rate[0]]
    new_arr_co2 = [i for i in arr if i[0] != gamma_rate[0]]
    n = 1
    while len(new_arr_ox) > 1:
        bits = [i[n] for i in new_arr_ox]
        if bits.count('1') >= bits.count('0'):
            new_arr_ox = [j for j in new_arr_ox if j[n] == '1']
        else:
            new_arr_ox = [j for j in new_arr_ox if j[n] == '0']
        n += 1
    
    n = 1
    while len(new_arr_co2) > 1:
        bits = [i[n] for i in new_arr_co2]
        if bits.count('1') >= bits.count('0'):
            new_arr_co2 = [j for j in new_arr_co2 if j[n] == '0']
        else:
            new_arr_co2 = [j for j in new_arr_co2 if j[n] == '1']
        n += 1
    
    print("Part 2:", int(new_arr_ox[0].strip(), 2) * int(new_arr_co2[0].strip(), 2))
   


    
