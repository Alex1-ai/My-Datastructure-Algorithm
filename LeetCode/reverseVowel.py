class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a','e','i','o','u']
        indexOfVowel = []
        count = 0
        while count < len(s):
            if s[count].lower() in vowels:
                print(s[count])
                indexOfVowel.append(count)
            count += 1
        # print("index " ,indexOfVowel)
        indexOfVowel.reverse()
        # print(indexOfVowel)
        counter = 0
        s = list(s)
        res = s.copy()
        # print(s)
        for i in range(len(s)):
            if s[i].lower() in vowels:
                # print("num" , indexOfVowel[counter])
                res[i]  = s[indexOfVowel[counter]]
                counter += 1
                

        print(res)
        return ''.join(res)





vowelReversed = Solution()
print(vowelReversed.reverseVowels("hello"))
print(vowelReversed.reverseVowels("leetcode"))

# class Solution(object):
#     def reverseVowels(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         vowels = set(['a', 'e', 'i', 'o', 'u'])
#         s = list(s)
        
#         left, right = 0, len(s) - 1

#         while left < right:
#             while left < right and s[left].lower() not in vowels:
#                 left += 1

#             while left < right and s[right].lower() not in vowels:
#                 right -= 1

#             # Swap the vowels
#             s[left], s[right] = s[right], s[left]

#             left += 1
#             right -= 1

#         return ''.join(s)

# # Example usage:
# vowelReversed = Solution()
# print(vowelReversed.reverseVowels("hello"))
# print(vowelReversed.reverseVowels("leetcode"))

# print(result)
