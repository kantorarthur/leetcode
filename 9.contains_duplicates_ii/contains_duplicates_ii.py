class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        duplicates = {}

        for i in range(0, len(nums)):
            if nums[i] in duplicates:
                if abs( duplicates.get(nums[i]) - i ) <= k:
                    return True
            duplicates[nums[i]] = i
        
        return False
        