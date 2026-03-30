class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            while (left < right && !alphaNum(s[left])) {
                left += 1;
            }

            while (left < right && !alphaNum(s[right])) {
                right -= 1;
            }

            if (tolower(s[left]) != tolower(s[right])) {
                return false;
            }

            left++;
            right--;
        }
        return true;
    }

    bool alphaNum(char c) {
        return (static_cast<int>('A') <= static_cast<int>(c) &&
            static_cast<int>(c) <= static_cast<int>('Z')) || 
            (static_cast<int>('a') <= static_cast<int>(c) &&
            static_cast<int>(c) <= static_cast<int>('z')) ||
            (static_cast<int>('0') <= static_cast<int>(c) &&
            static_cast<int>(c) <= static_cast<int>('9'));
    }
};
