class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int n = nums.size();

        if(n == 1)
        {
            if(nums[0] == k)
                return 1;
            return 0;
        }
        unordered_map<int, int> prefixes{};
        prefixes[0] = 1; 
        int prefixSum{};
        int numOfSubArrays{};

        for(int i{}; i < n; ++i)
        {
            prefixSum += nums[i];

            auto it = prefixes.find(prefixSum - k);
            if(it != prefixes.end())
                numOfSubArrays += it -> second;
            
            prefixes[prefixSum] += 1;
        }

        return numOfSubArrays;
    }
};