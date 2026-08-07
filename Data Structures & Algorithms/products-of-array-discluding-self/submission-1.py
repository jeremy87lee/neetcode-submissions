class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        Main_prod = math.prod(nums)
        array = []

        if Main_prod == 0:
            zero_count = 0
            zero_place = 0
            prod1 = 1
            for i in range(len(nums)):
                if nums[i] == 0:
                    zero_place = i
                    zero_count += 1
                    nums[i] = 1
                prod1 = prod1 * nums[i]
            if zero_count > 1:
                res = [0]*len(nums)
                return res
            res2 = [0]*len(nums)
            for i in range(len(nums)):
                if i == zero_place:
                    res2[i] = prod1
                else:
                    res2[i] = 0
            return res2


        if Main_prod != 0:
            for n in nums:
                output = Main_prod / n
                output = int(output)
                array.append(output)
            return array