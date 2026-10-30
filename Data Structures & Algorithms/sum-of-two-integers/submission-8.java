class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {                // repeat manipulation until b is 0
            int carry = (a & b) << 1;       // set/update carry var to ANDed a, b shifted once left
            a ^= b;                         // update a to itself XORed with b
            b = carry;                      // update b to carry val
        }
        return a;                       // return a
    }
}

// 01 + 01 = 10
// a     = 01, 00, {10}
// b     = 01, 10, 00
// carry = ui, 10, 00