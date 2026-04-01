def substring(data):
    left = 0
    longest_string = set()
    max_length = 0
    longest_chars = ""

    for right in range( len(data)):

        while data[right] in longest_string:
            longest_string.remove(data[left])
            left += 1
            print("inside while loop", longest_string)

        longest_string.add(data[right])
        if right - left + 1 > max_length:
            longest_chars = data[left:right+1]
            max_length = max(right -left+1, max_length)
        print("inside for loop ",longest_string)


    return max_length, longest_chars







# data = "abcabcbbdklsidkkfjdksdf"
# answr = substring(data)

# print(answr)


def longest_substring_k_distinct(data, k):

    left = 0
    max_length = 0
    memory = {}

    for right in range(len(data)):
        rightChar = data[right]
        memory[rightChar] = memory.get(rightChar, 0)+1

        print("memory for loop: " , memory)
        while len(memory) > k:
            leftChar = data[left]
            memory[leftChar] -= 1

            print("inside while loop", memory)

            if memory[leftChar] == 0:
                del memory[leftChar]
            left+=1

        max_length = max(right - left + 1, max_length)

    return max_length



# data = "abcabcbbdklsidkkfjdksdf"
data = "eceba"

answr = longest_substring_k_distinct(data, 2)

print(answr)
