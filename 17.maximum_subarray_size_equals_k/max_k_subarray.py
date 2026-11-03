def maximum_size_subarray_sum_equals_k(nums: list[int], k: int) -> int:
    max_size = 0
    mapp = {0 : -1}
    current_sum = 0
    for i in range(0, len(nums)):
        current_sum += nums[i]
        searching_sum = current_sum - k
        if searching_sum in mapp:
            curr_ind = i - mapp[searching_sum]
            max_size = max(max_size, curr_ind)
        if current_sum not in mapp:
            mapp[current_sum] = i
    return max_size

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    k = int(input())
    res = maximum_size_subarray_sum_equals_k(nums, k)
    print(res)
