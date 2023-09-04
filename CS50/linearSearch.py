def linearSearch(num, searchList):
    count = 0
    print(range(len(searchList))[-1])
    for i in range(len(searchList)):
        print(searchList[i] , " at index ", i)
        if num == searchList[i]:
            count+=1
            print("index is ", i, "and the value is ", searchList[i])
            print("It ran for ", count, " times")
            return
        count+=1
    print("Did not find the number")
        





linearSearch(30,[2,3,8,9,5,10,38,23,20,27])
