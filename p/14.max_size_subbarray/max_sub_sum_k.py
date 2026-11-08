class Solution:
    def maxSubArrayLen(self, nums: list[int], k: int) -> int:

        prefixes = {0 : -1}

        maxSubArray = 0
        prefix = 0

        for i in range(0, len(nums)):

            prefix += nums[i]
            if prefix - k in prefixes:
                maxSubArray = max(maxSubArray, i - prefixes[prefix - k])
            if prefix not in prefixes:
                prefixes[prefix] = i
        return maxSubArray
