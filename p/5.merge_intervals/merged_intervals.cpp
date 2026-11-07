class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if(intervals.size() == 1)
            return intervals;
        
        sort(intervals.begin(), intervals.end(), [](vector<int> &a, vector<int> &b)
                                                    {
                                                        return a[0] < b[0];
                                                    });
                                                
        vector<vector<int>> merged_intervals;

        for(auto i{0uz}; i < intervals.size(); ++i)
        {
            if(merged_intervals.size() == 0)
                merged_intervals.push_back(intervals[i]);
            else if(merged_intervals.back()[1] >= intervals[i][0] && merged_intervals.back()[1] < intervals[i][1])
            {
                merged_intervals.back()[1] = intervals[i][1];
            }
            else if(merged_intervals.back()[1] < intervals[i][0])
                merged_intervals.push_back(intervals[i]);
        }
        return merged_intervals;
    }
};