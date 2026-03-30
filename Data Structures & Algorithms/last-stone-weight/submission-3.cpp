class Solution {
public:
    vector<int>& smash(vector<int>& stones) {
        int first = 0;
        int fIdx;
        int second = 0;
        int sIdx;

        for (int i = 0; i < stones.size(); i++) {
            if (stones[i] > first) {
                first = stones[i];
                fIdx = i;
            }
        }
        
        vector<int> arr;
        for (int i = 0; i < stones.size(); i++) {
            if (i != fIdx) arr.push_back(stones[i]);
        }

        for (int i = 0; i < arr.size(); i++) {
            if (arr[i] > second) {
                second = arr[i];
                if (i >= fIdx) {
                    sIdx = i + 1;
                } else {
                    sIdx = i;
                }
            }
        }

    cout << "first: " << first << endl;
    cout << "fIdx: " << fIdx << endl;
    cout << "second: " << second << endl;
    cout << "sIdx: " << sIdx << endl;

        if (first == second) {
            if (fIdx > sIdx) {
                stones.erase(stones.begin() + fIdx);
                stones.erase(stones.begin() + sIdx);
            } else {
                stones.erase(stones.begin() + sIdx);
                stones.erase(stones.begin() + fIdx);
            }
        } else if (first < second) {
            stones[sIdx] = second - first;
            stones.erase(stones.begin() + fIdx);
        } else {
            stones[fIdx] = first - second;
            stones.erase(stones.begin() + sIdx);
        }

        if (stones.size() > 1)
            return smash(stones);
        else {
            return stones;
        }
    }

    int lastStoneWeight(vector<int>& stones) {
        if (stones.size() == 1) return stones[0];
        if (stones.empty()) return 0;
        vector<int> res = smash(stones);
        if (res.empty()) return 0;
        return res[0];
    }
};
