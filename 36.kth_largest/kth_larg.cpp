class Solution {
    void swap(int &a, int &b)
    {
        a = a ^ b;
        b = a ^ b;
        a = a ^ b;
    }

    void heapify(vector<int>& nums, int n, int i)
    {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        while(true)
        {
            largest = i;
            left = 2 * i + 1;
            right = 2 * i + 2;
            if(left < n && nums[left] > nums[largest])
                largest = left;
            if(right < n && nums[right] > nums[largest])
                largest = right;
            if(largest == i)
                break;
            swap(nums[largest], nums[i]);
            i = largest;
        }
    }

public:
    int findKthLargest(vector<int>& nums, int k) {
        
        int n = nums.size();
        for(int i{n / 2 - 1}; i >= 0; --i)
            heapify(nums, n, i);
        for(int i{}; i < k - 1; ++i)
        {
            swap(nums[0], nums[n - 1]);
            --n;
            heapify(nums, n, 0);
        }
        return nums[0];

    }
};