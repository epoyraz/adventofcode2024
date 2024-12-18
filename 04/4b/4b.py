def check_diagonal1(x, y, data, word):
    if x + len(word) > len(data) or y + len(word) > len(data[x]):
        return False
    for i in range(len(word)):
        if data[x+i][y+i] != word[i]:
            return False
    return True

def check_diagonal2(x, y, data, word):
    if x + len(word) > len(data) or y - len(word) < -1:
        return False
    for i in range(len(word)):
        if data[x+i][y-i] != word[i]:
            return False
    return True

def check_diagonal3(x, y, data, word):
    if x - len(word) < -1 or y + len(word) > len(data[x]):
        return False
    for i in range(len(word)):
        if data[x-i][y+i] != word[i]:
            return False
    return True

def check_diagonal4(x, y, data, word):
    if x - len(word) < -1 or y - len(word) < -1:
        return False
    for i in range(len(word)):
        if data[x-i][y-i] != word[i]:
            return False
    return True
    
# read sample.txt into 2d array
with open('input.txt') as f:
    data = f.readlines()
    # remove newline characters
    data = [x.strip() for x in data]
    xmas_count = 0
    word = "MAS"
    word2 = "SAM"
    for x in range(len(data)):
        for y in range(len(data[x])):
            if check_diagonal1(x,y, data, word) or check_diagonal1(x,y, data, word2):
                if check_diagonal3(x+2,y, data, word) or check_diagonal3(x+2,y, data, word2):
                    xmas_count += 1

print(xmas_count)