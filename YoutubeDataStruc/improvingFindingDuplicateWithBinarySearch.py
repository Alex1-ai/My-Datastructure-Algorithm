numbers = [3, 6, 2, 4, 3, 6, 8, 9]

# finding duplicate in the array


def findingDuplicateElement(arr):

    for i in range(len(arr)):
        lowestIndex, highestIndex = i+1, len(arr)-1
        while True:
            middleIndex = (lowestIndex + highestIndex)//2

            if arr[middleIndex] == arr[i]:
                print(
                    f" found a duplicate of {arr[i]} in position index at {i, middleIndex}")
                break
            elif arr[middleIndex] > arr[i]:
                highestIndex = middleIndex - 1
            elif arr[middleIndex] < arr[i]:
                lowestIndex = middleIndex + 1


findingDuplicateElement(numbers)
