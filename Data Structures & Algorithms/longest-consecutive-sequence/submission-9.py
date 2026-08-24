class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max = 1
        count = 1
        if nums == []:
            return 0
        if len(nums) == 1:
            return 1
        nums2 = sorted(nums)
        for i in range(len(nums)):
            if i != len(nums)-1:   
                if nums2[i] == nums2[i+1] - 1:
                    count += 1
                elif nums2[i] == nums2[i+1]:
                    continue
                else:
                    count = 1
                if count > max:
                    max = count
        return max 