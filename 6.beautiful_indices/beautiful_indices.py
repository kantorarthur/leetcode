def binary_search(arr: list, target: int) -> int:
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:

        a_sub = []
        b_sub = []

        beautiful_ind = []

        for i in range(0, len(s)):
            if s[i] == a[0]:
                cnt = 1
                a_ind = 1
                initial_i = i
                i += 1
                while i < len(s) and a_ind < len(a) and a[a_ind] == s[i]:
                    cnt += 1
                    i += 1
                    a_ind += 1
                if cnt == len(a):
                    a_sub.append(initial_i)
        
        for i in range(0, len(s)):
            if s[i] == b[0]:
                cnt = 1
                b_ind = 1
                initial_i = i
                i += 1
                while i < len(s) and b_ind < len(b) and b[b_ind] == s[i]:
                    cnt += 1
                    i += 1
                    b_ind += 1
                if cnt == len(b):
                    b_sub.append(initial_i)

        for i in a_sub:
            j = binary_search(b_sub, i - k)
            if j < len(b_sub) and b_sub[j] <= i + k:
                beautiful_ind.append(i)

        return beautiful_ind
        # a = [16, 33]
        # b = [4, 18]
        # k = 15

        


            
                 