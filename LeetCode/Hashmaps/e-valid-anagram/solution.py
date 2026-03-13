class Solution(object):
    def isAnagram(self, s, t):
        count = {}
        
        for c in s:
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1
        
        
        for c in t:
            if c in count:
                if count[c] == 1:
                    del count[c]
                else:
                    count[c] -= 1
            else:
                return False
        
        return True
        
        
s = "anagram"
t = "nagaram"

solution = Solution()
print(solution.isAnagram(s, t)) # should print true

# Time - O(n)
# Space - O{k) -> worst case is O(n)