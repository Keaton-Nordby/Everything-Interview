class Solution(object):
    def findClosestNumber(self, nums):

        if not nums:
            return None

        closest = nums[0]

        for num in nums:
            if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
                closest = num

        return closest
    
    
s = Solution()
print(s.findClosestNumber([-4, -2, 1, 4, 8]))  # Output: 1


# Time - O(n)
# Space - O(1)
