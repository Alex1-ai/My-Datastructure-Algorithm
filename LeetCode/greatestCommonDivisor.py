class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        len1, len2 = len(str1), len(str2)
        
        # Check if the concatenated strings are equal
        if str1 + str2 != str2 + str1:
            return ""
        
        # Find the greatest common divisor of lengths
        common_len = gcd(len1, len2)
        
        return str1[:common_len]

# Test cases
solution = Solution()
print(solution.gcdOfStrings("ABCABC", "ABC"))  # Output: "ABC"
print(solution.gcdOfStrings("ABABAB", "ABAB"))  # Output: "AB"
print(solution.gcdOfStrings("LEET", "CODE"))    # Output: ""
