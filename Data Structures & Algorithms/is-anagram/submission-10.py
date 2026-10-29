class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        temp = dict()
        for a,b in zip(s,t):
                temp[a] = temp.get(a,0) + 1
                temp[b] = temp.get(b,0) - 1
        for v in temp.values:
            if v != 0:
                return False
        return True