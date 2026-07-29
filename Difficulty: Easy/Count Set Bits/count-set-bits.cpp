class Solution {
  public:
    int setBits(int n) {
        int count = 0;
        while(n>0) {
            if (n&2 != 0) { //n%2 -> n&2. ig we have to change ==1 to !=0, "&" is not working with ==1
                count++;
            }
            n = n>>1; //substituted n/2 with n>>1
        }
        
        return count;
    }
};