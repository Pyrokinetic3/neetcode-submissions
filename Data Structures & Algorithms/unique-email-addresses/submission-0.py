class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        output = []
        for i in emails:
            original = i          # keep the original for the fixed-length loop
            temp = []
            for j in range(len(original)):
                if original[j] == '@':
                    temp.append(original[j:])
                    break
                if original[j] == '.':
                    continue
                if original[j] == '+':
                    k = j
                    while original[k] != '@':
                        k += 1
                    temp.append(original[k:])
                    break
                temp.append(original[j])
            output.append(''.join(temp))
        return len(set(output))