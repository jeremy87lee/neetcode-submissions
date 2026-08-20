class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashMap:
                if i < hashMap[diff]:
                    return [i,hashMap[diff]]
                else:
                    return [hashMap[diff],i]
            hashMap[nums[i]] = i