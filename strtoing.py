class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            if s[0].isdigit():
                return int(s)
            else:
                return 0
        sign = 1
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        if i >= len(s):
            return 0
        s = s[i:]
        if s[0].isalpha() == 1 or s[0] == ".":
            return 0
        i = 0
        if s[i] == "+" or s[i] == '-':
            if s[i + 1].isdigit() == 0:
                return 0
            if s[i] == "-":
                sign = 0
            i += 1
        s = s[i:]
        if s[0].isalpha() == 1 or s[0] == ".":
            return 0
        i = 0
        while i < len(s) and s[i].isdigit() == 1:
            i += 1
        s = s[:i]
        if sign == 1:
            s = int(s)
        else:
            s = -int(s)
        if abs(s) > 0x7fffffff:
            if sign == 0:
                return -(int(0x7fffffff) + 1)
            else:
                return int(0x7fffffff)
        return s
