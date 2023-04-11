class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for _ in range(numRows)]
        if len(s) == 1 or numRows == 1:
            return s
        for i in range(len(s)):
            row = (i + 1) % (2 * numRows - 2)
            if row <= numRows and row > 0:
                rows[row - 1].append(s[i])
            else:
                rows[(2 * numRows - 1 - row) % (2 * numRows - 2)].append(s[i])
        return ("".join([item for sublist in rows for item in sublist]))
