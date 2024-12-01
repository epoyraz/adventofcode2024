# read input.txt

lines = []
with open("input.txt") as f:
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

# iterate through col1 and count the number of occurences of each element in col2
similarity = []
for i in col1:
    similarity.append(i * col2.count(i))

print(sum(similarity))
