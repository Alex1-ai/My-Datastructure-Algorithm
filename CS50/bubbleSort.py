# sorting by pushing the highest value to the end
# bubble sort
def bubbleSort(sortList):

    for g in range(len(sortList)):
        swapped = False
        for i in range(len(sortList) -g - 1):
            if sortList[i] > sortList[i+1]:
                sortList[i+1],sortList[i]=sortList[i],sortList[i+1]
                swapped = True
        if not swapped:
            break
    print("sortList highest", sortList)


bubbleSort([8,3,2,9,1,39,8,2,20,38,10,12,14])