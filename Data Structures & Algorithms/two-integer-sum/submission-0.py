class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ''' 'BRUTE FORCE O(n^2)'
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    if i < j:
                        return [i,j]
                    return [j,i]'''
        'HASHING METHOD'
        hash = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hash:
                return [hash[diff],i]
            hash[n] = i
        return