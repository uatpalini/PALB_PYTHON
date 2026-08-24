class Solution {
  public:
    int maxSubarraySum(vector<int>& arr, int k) {
        int l = 0;
        int r = k-1;
        int sum = 0;
        int n = arr.size();
        int maxSum = 0;
        for(int i = l; i <= r; i++) {
            sum = sum + arr[i];
            maxSum = max(sum,maxSum);
        }
        while (r < n-1) {
            sum = sum - arr[l];
            l++;
            r++;
            sum = sum + arr[r];
            maxSum = max(sum,maxSum);
        }
        
        return maxSum;
    }
};