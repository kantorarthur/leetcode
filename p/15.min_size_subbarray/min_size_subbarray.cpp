class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        if(nums.size() == 1)
        {
            if(nums[0] >= target)
                return 1;
            return 0;
        }
        for(const auto& num : nums)
            if(num >= target)
                return 1;
        
        size_t left{};
        size_t right{1};

        int64_t currSum = nums[left] + nums[right];

        int currSubLen{2};
        int minSubLen{};

        int n{static_cast<int>(nums.size())};
        while(left < n && right < n)
        {
            if(left == right)
                ++right;
            if(currSum >= target)
            {
                if(minSubLen == 0 || currSubLen < minSubLen)
                    minSubLen = currSubLen;
                currSum -= nums[left];
                ++left;
                --currSubLen;
            }
            else
            {
                ++right;
                if(right >= n)
                    break;
                currSum += nums[right];
                ++currSubLen;
            }
        }
        return minSubLen;
    }
};