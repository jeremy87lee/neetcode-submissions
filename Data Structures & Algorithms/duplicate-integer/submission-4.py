class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """BRUTE FORCE 0(n^2)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i != j:
                    return True
        return False
        """
        'PATTERN - HASH USAGE O(n)'
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False