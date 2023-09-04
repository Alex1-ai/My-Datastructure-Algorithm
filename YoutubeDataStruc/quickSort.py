def swap(a, b, arr):
    # arr[a], arr[b] = arr[b], arr[a]
    # or
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp


def partition(elements, start_pointer, end_pointer):
    pivot_index = start_pointer
    pivot = elements[pivot_index]

    while start_pointer < end_pointer:

        while start_pointer < len(elements) and elements[start_pointer] <= pivot:
            # while elements is less than pivot keep on going

            start_pointer += 1

        # also working with end pointer the same concept
        while elements[end_pointer] > pivot:
            end_pointer -= 1

        # so making show the index has not cross to each other side
        if start_pointer < end_pointer:
            swap(start_pointer, end_pointer, elements)

    swap(pivot_index, end_pointer, elements)

    return end_pointer


def quick_sort(elements, start_pointer, end_pointer):
    if start_pointer < end_pointer:

        pi = partition(elements, start_pointer, end_pointer)

        # dividing the array and calling the quick sort on each side of the array
        quick_sort(elements, start_pointer, pi-1)  # left partition
        quick_sort(elements, pi+1, end_pointer)  # right partition


if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [20, 15, 20],
        [],
        [6]
    ]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)

    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f"sorted array: {elements}")
