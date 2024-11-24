class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        com = strs[0]
        j = len(com)
        for i in strs[1:]:
            while com != i[0:j]:
                j -= 1
                if j == 0:
                    return ""
                com = com[0:j]
        return com
