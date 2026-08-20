class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        arr = [[] for i in range(len(nums) + 1)]
        for n in nums:
            hashMap[n] = hashMap.get(n,0) + 1
        for n,h in hashMap.items():
            arr[h].append(n)
        res = []
        for i in range(len(arr)-1,0,-1):
            for a in arr[i]:
                res.append(a)
                if len(res) == k:
                    return res
        return res