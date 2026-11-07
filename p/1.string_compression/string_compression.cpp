class Solution {
public:
    int compress(vector<char>& chars) {

        int n = chars.size();

        int read{};
        int write{};

        int start{};

        char char_to_write{};

        int count{};
        while(read < n)
        {
            start = read;
            char_to_write = chars[read];
            while(read < n && chars[read] == chars[start])
                ++read;
            
            chars[write] = char_to_write;
            ++write;
            count = read - start;
            if(count > 1)
            {
                string cnt = to_string(count);
                for(auto const& c : cnt)
                {
                    chars[write] = c;
                    ++write;
                }
            }
        }
        return write;
    }
};