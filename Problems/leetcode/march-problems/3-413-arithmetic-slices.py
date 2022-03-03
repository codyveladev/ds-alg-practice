class Solution:
    def numberOfArithmeticSlices(self, nums) -> int:
        if len(nums) < 3: 
            return 0 
        #To keep track of the current diff to get a count
        curr_diff = -1 
        count = 0
        result = 0
        for i in range(1, len(nums)): 
            #Using memoization
            new_diff = nums[i] - nums[i - 1]
            if curr_diff != new_diff: 
                curr_diff = new_diff
                count = 1
            else: 
                result += count 
                count += 1
        return result  