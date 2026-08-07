class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        'PREFIX SUFFIX TECHNIQUE'
        pre_array = [0]*len(nums)
        suf_array = [0]*len(nums)
        product = 1
        for i in range(len(nums)):
            pre_array[i] = product
            product = product * nums[i]
        product = 1
        for i in range(len(nums)-1,-1,-1):
            suf_array[i] = product
            product = product * nums[i]
        res = [0]*len(nums)
        for i in range(len(nums)):
            n = pre_array[i]*suf_array[i]
            res[i] = n
        return res