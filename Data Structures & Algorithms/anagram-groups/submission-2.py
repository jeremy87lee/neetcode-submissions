class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for s in strs:
            sort = ''.join(sorted(s))
            hashMap[sort].append(s)
        return list(hashMap.values())