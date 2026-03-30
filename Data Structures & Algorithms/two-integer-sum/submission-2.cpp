class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hash;
        int diff;

        for (int i = 0; i < nums.size(); i++) {
            diff = target - nums[i];
            if (hash.count(diff)) {
                return {hash[diff], i};
            } else {
                hash[nums[i]] = i;
            }
        }
        return {0};
    }
};
