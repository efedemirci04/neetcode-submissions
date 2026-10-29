class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        temp = dict()
        temp2 = dict()
        for letter in s:
            if letter not in temp:
                temp[letter] = 1
            else:
                temp[letter] = temp.get(letter,0) + 1
        
        for letter in t:
            if letter not in temp2:
                temp2[letter] = 1
            else:
                temp2[letter] = temp2.get(letter,0) + 1
        if temp == temp2:
            return True
        return False