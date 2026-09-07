class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        if len(nums) == 1:
            return 1
        
        hashSet = set(nums)
        maximum = 0
        for h in hashSet:
            if h-1 not in hashSet:
                count = 1
                while h+1 in hashSet:
                    count += 1
                    h = h + 1
                if count > maximum:
                    maximum = count
        return maximum