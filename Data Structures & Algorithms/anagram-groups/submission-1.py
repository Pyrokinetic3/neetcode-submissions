class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        groups = {}
        sortedlist = strs.copy()
        for i, word in enumerate(sortedlist):
            sortedlist[i] = ''.join(sorted(word))
        for i, word in enumerate(sortedlist):
            if word not in groups:
                groups[word] = []
            groups[word].append(i)
        for i in groups.values():
            anagrams = []
            for k in i:
                anagrams.append(strs[k])
            output.append(anagrams)
        return output
                