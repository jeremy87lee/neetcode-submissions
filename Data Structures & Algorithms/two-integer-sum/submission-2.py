class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums:
                for j in range(len(nums)):
                    if nums[j] == diff and i != j:
                        if i > j:
                            return [j,i]
                        else:
                            return [i,j]