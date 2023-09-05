

def binarySearch(num, searchList):
    left = 0
    right = len(searchList)-1

    while left <= right:
        mid = (right+left)//2
        
        if searchList[mid] == num:
            return mid
        elif searchList[mid] > num:
             right = mid-1
        else:
            left = mid + 1

    
    return -1  # Element not found in the list

# Example usage:
result = binarySearch("iJeoma", ["abena", "belinda", "cashew", "Daire", "Futon", "George", "Hannah", "iJeoma", "jennifer", "Kamaela"])

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")



    



# binarySearch(7, [1,2, 3,4 ,5,6,7,8,9,10])



