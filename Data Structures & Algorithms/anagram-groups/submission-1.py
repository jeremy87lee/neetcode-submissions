class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for s in strs:
            s2 = ''.join(sorted(s))
            hashMap[s2].append(s)
        return list(hashMap.values())