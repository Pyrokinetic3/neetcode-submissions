class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        tracker = {}
        counter = 0
        for let in s1:
            if let not in tracker:
                tracker[let] = 1
            else:
                tracker[let] += 1
        tracker2 = tracker.copy()
        left = 0
        for i,let in enumerate(s2):
            if let not in tracker:
                tracker = tracker2.copy()
                counter = 0
                left = i + 1
            else:
                while tracker[let] == 0:
                    tracker[s2[left]] += 1
                    left += 1
                    counter -= 1
                tracker[let] -= 1
                counter += 1
            if counter == len(s1):
                return True
        return False