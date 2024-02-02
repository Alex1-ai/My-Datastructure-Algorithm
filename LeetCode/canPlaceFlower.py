class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == length-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1  # Plant a flower at the current plot
                count += 1

        return count >= n
    

flowerbed1 = Solution()
print(flowerbed1.canPlaceFlowers([1, 0, 0, 0, 1], 1))
print(flowerbed1.canPlaceFlowers([1, 0, 0, 0, 1], 2))