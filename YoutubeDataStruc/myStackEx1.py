from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return self.container == 0

    def size(self):
        return len(self.container)

    def reverse_string(self, s):
        stack = Stack()
        for ch in s:
            stack.push(ch)

        rstr = ''
        while stack.size() != 0:
            rstr += stack.pop()
        return rstr
    # def reverse_string(self, val):
    #     reverse = ""
    #     count = len(val)-1
    #     for letter in val:
    #         reverse += (val[count])
    #         count -= 1

    #     return reverse


def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch == '(' or ch == '{' or ch == '[':
            stack.push(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if stack.size() == 0:
                return False
            if not is_match(ch, stack.pop()):
                return False
    return stack.size() == 0


s = Stack()
# s.push(32)
# s.push(12)
# s.push(30)
# print(s.peek())
# print(s.pop())
# print(s.peek())
# print(s.container)
# print(s.is_empty())
# print(s.size())
print(s.reverse_string('good is the power of wisdom'))
print(is_balanced('({a+b})'))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+g))"))
print(is_balanced("[a+b]*(x+2y)* {gg+kk}"))
