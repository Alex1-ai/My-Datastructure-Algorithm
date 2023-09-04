"""
QUESTION 1: Alice has some cards with numbers written on them. 
She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. 
She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
 Write a function to help Bob locate the card.


       METHODS
    State the problem clearly. Identify the input & output formats.
    Come up with some example inputs & outputs. Try to cover all edge cases.
    Come up with a correct solution for the problem. State it in plain English.
    Implement the solution and test it using example inputs. Fix bugs, if any.
    Analyze the algorithm's complexity and identify inefficiencies, if any. 
    Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6 


"""


def locate_card(cards, query):
    pass


cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3


# we can test our function by passing the input
result = locate_card(cards, query)
print(result)

print(result == output)


test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

ans = locate_card(test['input']['cards'], test['input']

                  ['query']) == test['output']
print(ans)
# or using this
ans = locate_card(**test['input']) == test['input']
print(ans)


tests = []

# query occrus in the middle
tests.append(test)
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})


# query is the first element

tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

# query is the last element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

# cards contains just one element, query
tests.append({
    'input': {
        'cards': [6],
        'query': 6

    },
    'output': 0
})


# cards does not contain query

tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -1],
        'query': 4
    },
    'output': -1
})


# cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})


# numbers can repeat in cards

tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7

})

# query occurs multiple times

tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2

})

print(tests)


def locate_card(cards, query):
    # create a variable position with the value 0

    position = 0

    # set up a loop for repetition
    while position < len(cards):

        # check if element at the current position jmatch the query
        if cards[position] == query:

            # answer found! Return and exit..
            return position

        # increment the position
        position += 1

        # check if we have reached the end of the array
        if position == len(cards):

            # number not found, return -1
            return -1
    return -1


result = locate_card(test['input']['cards'],
                     test['input']['query']) == test['output']
print(result)

for test in tests:
    ans = locate_card(**test['input']) == test['output']
    print(ans)
