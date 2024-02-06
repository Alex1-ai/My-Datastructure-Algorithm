class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # print(s.split())
        # # print(s.strip())
        # print(s)
        res = s.split()
        res = res[::-1]
        print(res)
        # print("".join(res))

        return " ".join(res)






result = Solution()
print(result.reverseWords("the sky is blue"))
print(result.reverseWords("  hello world  "))
print(result.reverseWords("a good   example"))
