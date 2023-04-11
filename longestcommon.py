class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < len(min(out, strs[i])) and out[j] == strs[i][j]:
                j+=1
            out = out[:j]
        return out