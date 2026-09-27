class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n = nums.size();
        int left = 0; int right = n-1;
        vector<int> ans(n);
        for(int pos = n - 1; pos > -1; pos--) {
            int leftsq = nums[left] * nums[left];
            int rightsq = nums[right] * nums[right];
            if (leftsq > rightsq) {
                ans[pos] = leftsq;
                left++;
            } else {
                ans[pos] = rightsq;
                right--;
            }
        }
        return ans;
    }
};