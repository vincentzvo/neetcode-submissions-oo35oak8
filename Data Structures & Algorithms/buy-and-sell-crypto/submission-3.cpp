class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0;
        int r = 1;
        int max = 0;

        while (r < prices.size()) {
            if (prices[r] < prices[l]) {
                l = r;
            } else if (prices[r] - prices[l] > max){
                max = prices[r] - prices[l];
            }
            r++;
        }
        return max;
    }
};
