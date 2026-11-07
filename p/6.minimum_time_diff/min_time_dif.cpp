class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        vector<int> convertedTime;

        string currHour;
        string currMinute;

        for(auto i{0uz}; i < timePoints.size(); ++i)
        {
            currHour = "\0";
            currMinute = "\0";
            for(auto j{0uz}; j < timePoints[i].size(); ++j)
            {
                while(j < timePoints[i].size() && timePoints[i][j] != ':')
                    currHour.push_back(timePoints[i][j++]);
                ++j;
                while(j < timePoints[i].size() && timePoints[i][j])
                    currMinute.push_back(timePoints[i][j++]);
            }
            convertedTime.push_back(stoi(currHour) * 60 + stoi(currMinute));
        }

        sort(convertedTime.begin(), convertedTime.end());

        int min_dif{1440 - convertedTime.back() + convertedTime.front()};

        for(auto i{1uz}; i < convertedTime.size(); ++i)
        {
            if(convertedTime[i] - convertedTime[i - 1] < min_dif)
                min_dif = convertedTime[i] - convertedTime[i - 1];
        }
        return min_dif;
    }
};