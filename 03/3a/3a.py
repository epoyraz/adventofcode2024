#read input.txt line by line and loop through each line
with open('input.txt') as f:
    data = f.readlines()

    total = 0
    
    for line in data:
    # regexp extract all occurences of  "mul(\\d+, \\d+)" from the first line"
        import re
        m = re.findall(r"mul\(\d+,\d+\)", line)
        print(m)

        # extract the first and the second digit from mul(3, 4)
        m = re.findall(r"mul\((\d+),(\d+)\)", line)
        print(m)

        # iterate through list and convert tuple of string to tuple of ints
        for i in range(len(m)):
            m[i] = (int(m[i][0]), int(m[i][1]))
        
        # iterate through list and multiply the two numbers and save it in the list
        for i in range(len(m)):
            m[i] = m[i][0] * m[i][1]
        print(m)
        
        #print the sum of the list
        total += sum(m)

print(total)