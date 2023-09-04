

numbers = [4, 9, 5, 21, 10, 57, 68, 91]
ans = 10
print(ans not in numbers)


def myLinkedList(arr, ans):
    print(arr)
    arr.sort()
    print(arr)
    lowestIndex = 0
    highestIndex = len(arr) - 1
    count = 0

    if ans not in arr:
        return "number not in array"
    while True:
        count += 1
        middleIndex = ((lowestIndex+highestIndex)//2)
        if arr[middleIndex] == ans:
            return f"found number just in {count} iterations"
            break
        elif arr[middleIndex] > ans:
            highestIndex = middleIndex - 1

        elif arr[middleIndex] < ans:
            lowestIndex = middleIndex + 1


print(myLinkedList(numbers, ans))
