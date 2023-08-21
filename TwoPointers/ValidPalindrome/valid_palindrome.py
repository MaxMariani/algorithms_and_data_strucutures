class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ns = ""
        for l in s:
            if l >= 'a' and l <= 'z' or l >= '0' and l <= '9':
                ns += l
        left, right = 0, len(ns) -1
        while left < right:
            if ns[left] != ns[right]:
                return False
            left += 1
            right -= 1
        return True
        
