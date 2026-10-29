class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            duplicate = False
            for j in range(len(s)):
                if i != j and s[i] == s[j]:
                    duplicate = True
                    break

            if not duplicate:
                return i

        return -1 