class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Hashlist = list()
        for n in nums:
            if n in Hashlist:
                return True
            Hashlist.append(n)
        return False