
# def isValid(data):
#     stack = []

#     mapping = {
#         ")":"(",
#         "]":"[",
#         "}":"{"
#     }

#     for char in data:
#         print(char)
#         if char in mapping:
#             top = stack.pop() if stack else "#"
#             print("top" , top)
#             print("mapping data", mapping[char])
#             if mapping[char] != top:
#                 return False
#         else:
#             stack.append(char)
#             print("stack", stack)

#     return len(stack) == 0


def isValid(s: str) -> bool:

    if len(s) == 0:
        return True   # empty string is valid

    stack = []

    mapping = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in s:
        if char in mapping:  # closing bracket
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            stack.append(char)

    return len(stack) == 0




answer = isValid("]()[{}")

print("answer: ",answer)
