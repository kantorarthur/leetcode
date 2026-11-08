class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        dups = {}

        for i in range(0, len(nums)):
            if nums[i] in dups:
                if abs(i - dups[nums[i]]) <= k:
                    return True
            dups[nums[i]] = i
        return False
        