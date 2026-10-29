class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp1 = set()
        
        for w in s:
            temp1.add(w)
        for w in t:
            if w not in temp1:
                return False
        return True