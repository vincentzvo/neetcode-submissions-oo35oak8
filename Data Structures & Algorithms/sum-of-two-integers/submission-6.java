class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            var carry = a;
            a = a ^ b;
            b = (carry & b) << 1;
        }
        return a;
    }
}
