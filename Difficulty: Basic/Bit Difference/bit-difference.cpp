class Solution {
  public:
    int countBitsFlip(int a, int b) {
        int x = a^b;
        int count = 0;
        while (x>0) {
            if (x&2 != 0) {
                count++;
            }
            x = x>>1;
        }
        
        return count;
    }
};