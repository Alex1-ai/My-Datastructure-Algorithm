"""
1768. Merge Strings Alternately
Easy
Topics
Companies
Hint
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.






"""


class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        if len(word1) == 0 and len(word2) > 0:
            print(word2)
            return word2
        elif len(word2) == 0 and len(word1) > 0:
            print(word1)
            return word1
        elif len(word1) == 0 and len(word2) == 0:
            return False
        
        list = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                print(word1[i])
                list.append(word1[i])
            
            if i < len(word2):
                print(word2[i])
                list.append(word2[i])
            i += 1

            # print(list)

        # print(list)
        # print("".join(list))
        
        return "".join(list)



merge = Solution()
# merge.mergeAlternately("abc","pqr")
# merge.mergeAlternately("abcd","pq")
# merge.mergeAlternately("ab","zqrc")
print(merge.mergeAlternately("","zqrc"))
print(merge.mergeAlternately("bdce",""))


# OR use this alternative
# class Solution(object):
#     def mergeAlternately(self, word1, word2):
#         result = [word1[i] + word2[i] for i in range(min(len(word1), len(word2)))]
#         result.extend(word1[len(word2):] + word2[len(word1):])
#         return ''.join(result)
