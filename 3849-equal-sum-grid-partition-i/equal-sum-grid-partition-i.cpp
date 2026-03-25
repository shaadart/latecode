class Solution {
public:
    bool canPartitionGrid(vector<vector<int>>& grid) {
        vector<int> rows, cols;
        int n = grid.size(), m = grid[0].size();
        long long rowsum = 0, colsum = 0;

        for(int i = 0; i < n; i++){
            long long r = 0;
            for(int j = 0; j < m; j++){
                r += grid[i][j];
            }
            rows.push_back(r);
            rowsum += r;
        }

        for(int i = 0; i < m; i++){
            long long c = 0;
            for(int j = 0; j < n; j++){
                c += grid[j][i];
            }
            cols.push_back(c);
            colsum += c;
        }

        long long currRow = 0, currCol = 0;
        for(int i = 0; i < n; i++){
            currRow += rows[i];
            long long diff = rowsum - currRow;
            if(diff == currRow) return true;
        }

        for(int j = 0; j < m; j++){
            currCol += cols[j];
            long long diff = colsum - currCol;
            if(diff == currCol) return true;
        }

        return false;
        
    }
};