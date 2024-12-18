# take an array of ints and check if all numbers are decreasing
def check_decreasing(arr):
    for i in range(1, len(arr)):
        if arr[i] >= arr[i-1]:
            return False
    return True
    
# take an array of ints and check if all numbers are increasing
def check_increasing(arr):
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            return False
    return True

# check if Any two adjacent levels differ by at least one and at most three.
def check_adjacent(arr):
    for i in range(1, len(arr)):
        if abs(arr[i] - arr[i-1]) > 3:
            return False
    return True

#read input.txt line by line and loop through each line
with open('input.txt') as f:
    data = f.readlines()

    safe_reports = 0
    # loop through each line
    for line in data:
        safe = True
        decreasing = check_decreasing( [int(x) for x in line.split()])
        increasing = check_increasing( [int(x) for x in line.split()])
        adjacent = check_adjacent( [int(x) for x in line.split()])

        # print "not safe" if decreasing or increasing is false
        if not decreasing and not increasing:
            print(line)
            print("not safe")
            safe = False
        
        if not adjacent:
            print(line)
            print("not safe")
            safe = False

        if safe:
            print(line)
            safe_reports += 1

    print(safe_reports)

