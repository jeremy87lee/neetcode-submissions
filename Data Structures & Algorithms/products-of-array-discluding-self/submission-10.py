class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suf_array = [0 for i in range(len(nums))]
        pre_array = []
        res = []

        product = 1
        for i in range(len(nums)):
            pre_array.append(product)
            product = product * nums[i]
        
        product = 1
        for i in range(len(nums)-1,-1,-1):
            suf_array[i] = (product)
            product = product * nums[i]
        
        for i in range(len(suf_array)):
            res.append(suf_array[i]*pre_array[i])
        return res