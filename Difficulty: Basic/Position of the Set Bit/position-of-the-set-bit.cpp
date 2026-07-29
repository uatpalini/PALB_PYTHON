class Solution {
  public:
    int findPosition(int n) {
            int count = 0;
            int x = 0;
            int p = 0;
            while (n>0) {
                p++;
                if (n&1 != 0) {
                    count ++;
                    x = p;
                }
                n = n>>1;
            }
            if(count == 1) {
                    return x;
                }
                else {
                    return -1;
                }
    }
};