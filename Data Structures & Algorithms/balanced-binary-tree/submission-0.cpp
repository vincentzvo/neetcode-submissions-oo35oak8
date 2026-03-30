/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    pair<bool, int> dfs(TreeNode* root) {
        bool balanced;
        
        if (!root) {
            return {true, 0};
        }

        pair<bool, int> left = dfs(root->left);
        pair<bool, int> right = dfs(root->right);

        if (left.first && right.first && abs(left.second - right.second) <= 1) {
            balanced = true;
        } else {
            balanced = false;
        }

        return {balanced, 1 + max(left.second, right.second)};
    }

    bool isBalanced(TreeNode* root) {
        return dfs(root).first;
    }
};
