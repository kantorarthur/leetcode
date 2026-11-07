class Solution {
public:
    void findAppearance(vector<int>& store_vec, const string& str, const string& sub_str){

        size_t i{};
        size_t j{};

        int curr_len{};
        int initial_i{};

        while(i < str.size())
        {
            curr_len = 0;
            j = 0;
            initial_i = i;
            while(i < str.size() && j < sub_str.size() && str[i] == sub_str[j])
            {
                ++curr_len;
                ++j;
                ++i;
            }
            if(curr_len == sub_str.size())
                store_vec.push_back(initial_i);
            i = initial_i + 1;
        }
    }

    int binary_search(const vector<int>& arr, int target)
    {
        int left{};
        int right = arr.size();
        int mid = left + (right - left) / 2;
        while(left < right)
        {
            mid = left + (right - left) / 2;
            if(arr[mid] < target)
                left = mid + 1;
            else
                right = mid;
        }
        return left;
    }

    vector<int> beautifulIndices(string s, string a, string b, int k) {
        vector<int> app_a;
        vector<int> app_b;
        findAppearance(app_a, s, a);
        findAppearance(app_b, s, b);
        
        vector<int> beautiful_indices;
        for(const auto& i : app_a)
        {
            int j = binary_search(app_b, i - k);
            if(j < app_b.size() && app_b[j] <= i + k)
                beautiful_indices.push_back(i);
        }
        return beautiful_indices;
    }
};