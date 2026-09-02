class NumMatrix {
public:
    vector<vector<int>> pfix;

    NumMatrix(vector<vector<int>>& matrix) {
        pfix=matrix;
        int m = matrix.size();
        int n = matrix[0].size();

        for (int i = 0; i < m; i++) {
            int sum = 0;
            for (int j = 0; j < n; j++) {
                sum = sum + pfix[i][j];
                pfix[i][j] = sum;
            }
        }

        for (int i = 0; i < n; i++) {
            int sum = 0;
            for (int j = 0; j < m; j++) {
                sum = sum + pfix[j][i];
                pfix[j][i] = sum;
            }
        }

    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
int sum2 = pfix[row2][col2];        
        if (row1 > 0) {
            sum2 = sum2 - pfix[row1-1][col2];
        }
        if(col1 > 0) {
            sum2 = sum2 - pfix[row2][col1-1];
        } 
        if (col1 > 0 && row1 > 0) {
            sum2 = sum2 + pfix[row1-1][col1-1];
        }

        return sum2;
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */