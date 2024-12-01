# read input.txt

lines = []
with open('input.txt') as f:
    lines = f.readlines()

# col1
col1 = []
for line in lines:
    col1.append(int(line.split()[0]))

# col2
col2 = []
for line in lines:
    col2.append(int((line.split()[1])))

col1.sort()
col2.sort()

# zip col1 and col2 and subtract the two values and take absolute value
# then sum all the values
sum = 0
for i in range(len(col1)):
    sum += abs(col1[i] - col2[i])

print(sum)