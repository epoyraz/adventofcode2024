with open('input.txt') as f:
    data = f.readlines()
    
    # first line
    lines = data

    total = 0

    pruned = []

    for line in lines:
        while line.find("don't(") != -1:
            x = line.find("don't()")
            y = line.find("do()", x)
            if x != -1 and y == -1:
                line = line[:x]
                continue
            if x != -1 and y != -1:
                line = line[:x] + line[y+4:]
                continue
            else:
                print(x,y)
        pruned.append(line)
    
    print(pruned)

    for x in pruned:
        print(x.find("don't"))
    
    for line in pruned:
    # regexp extract all occurences of  "mul(\\d+, \\d+)" from the first line"
        import re
        m = re.findall(r"mul\(\d+,\d+\)", line)
        #print(m)

        # extract the first and the second digit from mul(3, 4)
        m = re.findall(r"mul\((\d+),(\d+)\)", line)
        #print(m)

        # iterate through list and convert tuple of string to tuple of ints
        for i in range(len(m)):
            m[i] = (int(m[i][0]), int(m[i][1]))
        
        # iterate through list and multiply the two numbers and save it in the list
        for i in range(len(m)):
            m[i] = m[i][0] * m[i][1]
        #print(m)
        
        #print the sum of the list
        total += sum(m)

print(total)