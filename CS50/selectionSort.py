
# sorting the smallest one to the right
def selectionSort(sortList):
    # smallest = 0
    for g in range(len(sortList)):
        smallest = g
        for i in range(g + 1,len(sortList)):
            print("hery",sortList[smallest])
            if sortList[smallest] > sortList[i]:
                smallest = i

        
    
    
        print("index ", smallest)
        sortList[g],sortList[smallest] = sortList[smallest], sortList[g]
        print(sortList)
    print(sortList)





selectionSort([8,3,2,9,1,39,8,2,20,38,10,12,14])