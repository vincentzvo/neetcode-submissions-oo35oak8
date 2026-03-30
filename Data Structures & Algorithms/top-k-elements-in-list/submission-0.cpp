class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> hash;
        for (int n : nums) {
            hash[n]++;
        }

        vector<int> res;
        for (int i = 0; i < k; i++) {
            auto max = hash.begin();
            for (auto it = hash.begin(); it != hash.end(); it++) {
                if (it->second > max->second) {
                    max = it;
                }
            }
            res.push_back(max->first);
            hash.erase(max);
        }

        return res;
    }
};
