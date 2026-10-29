class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        temp = dict()
        temp2 = dict()
        for letter in s:
                temp[letter] = temp.get(letter,0) + 1
        
        for letter in t:
                temp2[letter] = temp2.get(letter,0) + 1
        return temp == temp2