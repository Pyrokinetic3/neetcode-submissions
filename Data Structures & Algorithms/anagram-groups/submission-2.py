class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}
        s_output = []
        output = []
        for i in strs:
            s_output.append(''.join(sorted(i)))
        for i,k in enumerate(s_output):
            if k not in count:
                count[k] = [i]
            else:
                count[k].append(i)
        for i in count:
            output.append([strs[k] for k in count[i]])
        return output