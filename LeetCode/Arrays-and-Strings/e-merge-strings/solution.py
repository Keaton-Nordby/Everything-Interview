class Solution(object):
    def mergeAlternately(self, word1, word2):
        
        l, r = 0, 0
        res = ""
        
        while l < len(word1) and r < len(word2):
            res += word1[l]
            res += word2[r]
            l += 1
            r += 1
            
        while l < len(word1):
            res += word1[l]
            l += 1
                
        while r < len(word2):
            res += word2[r]
            r += 1
                
        return res
            
            
            
                
        


s = Solution()
print(s.mergeAlternately(word1="ttt", word2="ccccccc"))  # Output: tctctctcccc


# Time Complexity - O(n)
# Space Complexity - O(1)