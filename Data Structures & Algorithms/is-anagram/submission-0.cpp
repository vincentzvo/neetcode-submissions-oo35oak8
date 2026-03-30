class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        vector<char> v;
        vector<char> u;

        for (char c : s) {
            v.push_back(c);
        }

        for (char h : t) {
            u.push_back(h);
        }

        sort(v.begin(), v.end());
        sort(u.begin(), u.end());

        for (int i = 0; i < v.size(); i++) {
            if(v[i] != u[i]) {
                return false;
            }
        }

        return true;
    }
};
