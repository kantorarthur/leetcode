class WordDistance {
private:
    unordered_map<string, vector<int>> word_app;
public:
    WordDistance(vector<string>& wordsDict) {
        for(auto i{0uz}; i < wordsDict.size(); ++i)
        {
            word_app[wordsDict[i]].push_back(i);
        }
    }
    
    int shortest(string word1, string word2) {
        auto word1_positions = word_app.at(word1);
        auto word2_positions = word_app.at(word2);

        size_t i{};
        size_t j{};
        int best{numeric_limits<int>::max()};
        while(i < word1_positions.size() && j < word2_positions.size())
        {
            if(abs(word1_positions[i] - word2_positions[j]) < best)
                best = abs(word1_positions[i] - word2_positions[j]);
            if(word1_positions[i] < word2_positions[j])
                ++i;
            else
                ++j;
        }
        return best;
    }
};

/**
 * Your WordDistance object will be instantiated and called as such:
 * WordDistance* obj = new WordDistance(wordsDict);
 * int param_1 = obj->shortest(word1,word2);
 */