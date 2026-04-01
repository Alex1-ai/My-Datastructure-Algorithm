def brute_force_two_sum(data, target):
    print("Begin solving")
    for i in range(len(data) ):
        for j in range(len(data)):
            if i != j and data[i] + data[j] == target:
                print(data[j])
                print(data[i])
                return i, j



def optimized_two_sum(data, target):
    if data == None or len(data) == 0:
        return

    seen = {}
    seen[data[0]] = 0
    for i in range(1, len(data)):
        print(seen)

        difference = target - data[i]
        print(difference)
        if difference in seen:
            print(difference, data[i])
            return seen[difference], i
        seen[data[i]] = i


def sorted_two_sum(data, target):
    print("Sorted arrays")
    right = 0
    left = len(data)-1
    # print(right, left)
    # for i in range(len(data)):
    while left < right:
        sum = data[right] + data[left]
        if sum > target:
            left-=1
        elif sum < target:
            right+=1

        elif sum == target:
            return right, left





answer = sorted_two_sum([1,2,3,4, 5,6,7, 8,9,10,12, 13, 14], 12)
print("index for the two number is ", answer)
# answer = optimized_two_sum([1,5,3,6,7], 9)
# print("index for the two number is ", answer)
# answer = brute_force_two_sum([2,11,15,9,7], 9)
# print("index for the two number is ", answer)




