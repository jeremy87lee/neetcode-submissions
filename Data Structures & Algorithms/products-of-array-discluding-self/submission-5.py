class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_array = [0]*len(nums)
        suf_array = [0]*len(nums)
        res = [0]*len(nums)
        product = 1
        for i in range(len(nums)):
            pre_array[i] = product
            product = product * nums[i]
        product = 1
        for i in range(len(nums)-1,-1,-1):
            suf_array[i] = product
            product = product * nums[i]
        for i in range(len(nums)):
            res[i] = suf_array[i]*pre_array[i]
        return res