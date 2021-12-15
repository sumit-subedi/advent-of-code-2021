from collections import defaultdict, Counter
with open('input.txt', 'r') as f:
    content = f.readlines()
    string = content[0].strip()
    command = [i.strip() for i in content[2:]]
    worddict = {}
    contentdict = defaultdict(lambda: 0)
    for i in command:
        org, rep = i.split(' -> ')
        worddict[org] = rep
    # print(worddict, string)
    for i in range(len(string) - 1):
        contentdict[string[i]+string[i+1]] += 1
        
    counter = Counter()
    for _ in range(40):
        newdict = defaultdict(lambda : 0)
        for i, quantity in contentdict.items():
            
            new = i[0]+worddict[i]+i[1]
            
            newdict[new[0]+new[1]] += quantity
            newdict[new[1]+new[2]] += quantity

        contentdict = newdict
            
        # print(sum([i*2 for i in contentdict.values()]))
        
    
    
    for pair, quantity in contentdict.items():
        counter[pair[0]] += quantity
    counter[pair[1]] += 1
        
    
    print(max(counter.values()) - min(counter.values()))



    
