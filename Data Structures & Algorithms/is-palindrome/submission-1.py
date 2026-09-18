class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(filter(str.isalnum, s)).lower()
        k = len(clean) - 1
        j = 0
        while j < k:
            if clean[k] == clean[j]:
                k -= 1
                j += 1
            else:
                return False
        return True