class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rtracker = {}
        mtracker = {}
        for i in ransomNote:
            if i in rtracker:
                rtracker[i] += 1
            else:
                rtracker[i] = 0
        for i in magazine:
            if i in mtracker:
                mtracker[i] += 1
            else:
                mtracker[i] = 0
        for i in rtracker:
            if i not in mtracker:
                return False
            else:
                if rtracker[i] > mtracker[i]:
                    return False
        return True