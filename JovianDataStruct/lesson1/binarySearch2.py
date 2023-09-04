from re import L


def locate_card(card, query):
    lo, hi = 0, len(card)-1

    while lo <= hi:
        mid = (lo + hi)//2
        mid_number = card[mid]

        print("lo: ", lo, ", hi:", hi, ", mid:",
              mid, ", mid_number:", mid_number)

        if mid_number == query:

            return mid
        elif mid_number < query:
            hi = mid - 1
        elif mid_number > query:
            lo = mid + 1

    return -1


cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 10

print(locate_card(cards, query))
