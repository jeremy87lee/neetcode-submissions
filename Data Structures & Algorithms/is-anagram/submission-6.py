class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap1 = {}
        hashMap2 = {}
        if len(s) != len(t):
            return False
        for c in s:
            hashMap1[c] = 1 + hashMap1.get(c,0)
        for c in t:
            hashMap2[c] = 1 + hashMap2.get(c,0)
        for c in s:
            if hashMap1[c] != hashMap2.get(c,0):
                return False
        return True