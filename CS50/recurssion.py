# Printing a triangle

def triangle():
    height = int(input("Enter in the size"))
    print( type(height))
    i =0
    while i < height:
        j=0
        while j < i + 1:
            # print(i)
            print("#", end=" ")

            j+=1
        print()
        i+=1

triangle()


# using recurrsion to do that

def recurTriangle(height):
    if height <= 0:
        return
    
    
    count = height
    while count <= height:
         print("#", end=" ")
         count -=1
    print()
    recurTriangle(height-1)


height = int(input("Input the height of the triangle: "))
recurTriangle(height)