class Solution(object):
    def containsDuplicate(self, nums):
        

        seen = {}

        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                return True
        return False
    
    
nums = [1,2,3,1]
s = Solution()
print(s.containsDuplicate(nums)) # should print true
