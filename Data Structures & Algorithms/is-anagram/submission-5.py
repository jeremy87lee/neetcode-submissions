class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}
        hashMap2 = {}

        if len(s) != len(t):
            return False

        for c in s:
            hashMap[c] = hashMap.get(c,0) + 1
        
        for c in t:
            hashMap2[c] = hashMap2.get(c,0) + 1
        
        for h in hashMap:
            if hashMap[h] != hashMap2.get(h,0):
                return False
        return True