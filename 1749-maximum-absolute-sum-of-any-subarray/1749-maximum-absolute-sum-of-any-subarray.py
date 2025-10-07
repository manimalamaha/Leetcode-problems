class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum=min_sum=curr_max=curr_min=0
        for num in nums:
            curr_max=max(num,curr_max+num)
            curr_min=min(num,curr_min+num)
            max_sum=max(curr_max,max_sum)
            min_sum=min(curr_min,min_sum)
        return max(max_sum,abs(min_sum))