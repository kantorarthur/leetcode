class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        map = {}

        for num in nums:
            map[num] = map.get(num, 0) + 1
        
        bucket = [ [] for i in range(0, len(nums) + 1) ]

        for num, freq in map.items():
            bucket[freq].append(num)
        
        ret_list = []

        for i in range( len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                ret_list.append(num)
                
                if len(ret_list) == k:
                    return ret_list
        