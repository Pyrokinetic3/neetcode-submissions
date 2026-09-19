class Solution:
    def isPathCrossing(self, path: str) -> bool:
        a, b = 0, 0
        tracker = [[0,0]]
        for i in path:
            if i == 'N':
                a += 1
            elif i == 'S':
                a -= 1
            elif i == 'E':
                b += 1
            elif i == 'W':
                b -= 1
            loc = [a,b]
            if loc in tracker:
                return True
            tracker.append(loc)
        return False

