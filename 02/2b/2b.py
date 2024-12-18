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

# given a list of ints return the list without the xth element
def remove_index(arr, x):
    return arr[:x] + arr[x+1:]

#read input.txt line by line and loop through each line
with open('input.txt') as f:
    data = f.readlines()

    safe_reports = 0
    # loop through each line
    for line in data:
        safe = True
        ints = [int(x) for x in line.split()]
        decreasing = check_decreasing(ints)
        increasing = check_increasing(ints)
        adjacent = check_adjacent(ints)

        # print "not safe" if decreasing or increasing is false
        if not decreasing and not increasing:
            print(line)
            print("not safe")
            safe = False
        
        if not adjacent:
            print(line)
            print("not safe")
            safe = False

        if not safe:
            for x in range(len(ints)):
                new_list = remove_index(ints, x)
                decreasing = check_decreasing(new_list)
                increasing = check_increasing(new_list)
                adjacent = check_adjacent(new_list)

                if decreasing and adjacent:
                    safe = True
                    break

                if increasing and adjacent:
                    safe = True
                    break

        if safe:
            #print(line)
            safe_reports += 1

    print(safe_reports)

