class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in hashMap and i != hashMap.get(diff):
                if hashMap.get(diff) > i:
                    return [i,hashMap.get(diff)]
                else:
                    return [hashMap.get(diff),i]
            hashMap[n] = i