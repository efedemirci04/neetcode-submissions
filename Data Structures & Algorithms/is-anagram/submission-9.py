class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        temp = dict()
        temp2 = dict()
        for a,b in zip(s,t):
                temp[a] = temp.get(a,0) + 1
                temp2[b] = temp2.get(b,0) + 1
        return temp == temp2