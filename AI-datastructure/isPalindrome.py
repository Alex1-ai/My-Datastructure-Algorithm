# def isPalindrome(num):
#     return str(num) == str(num)[::-1]


def isPalindrome(num):
    if num < 0 or (num % 10 == 0 and num != 0):
        return False

    reversed_half = 0
    while num > reversed_half:
        reversed_half = reversed_half * 10 + num % 10
        num //= 10

    return num == reversed_half or num == reversed_half // 10





print(isPalindrome(121))
print(isPalindrome(-121))
