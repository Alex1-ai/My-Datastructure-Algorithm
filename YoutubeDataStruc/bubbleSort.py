def bubble_sort(elements):
    size = len(elements)

    # because you want to compare but not including the
    # last element 'size -1 '

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    elements = [5, 9, 2, 1, 67, 34, 88, 34]


bubble_sort(elements)
print(elements)
