class Solution(object):
    def longestCommonPrefix(self, strs):
        
        
        min_length = float("inf")
        
        for s in strs:
            if len(s) < min_length:
                min_length = len(s)
        
        i = 0
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1
        
        return s[:1]        
        

strs = ["flower","flow","flight"]      
s = Solution()
print(s.longestCommonPrefix(strs))

# Time - O(n * m)
# Space - O(1)
