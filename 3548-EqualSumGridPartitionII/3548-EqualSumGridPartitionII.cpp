// Last updated: 3/27/2026, 12:31:21 AM
1class Solution {
2public:
3    bool canPartitionGrid(vector<vector<int>>& grid) {
4        int m = grid.size(), n = grid[0].size();
5
6        long long total = 0;
7        unordered_map<long long,int> bottomMap,topMap, leftMap, rightMap;
8
9        // Initialize bottomMap and rightMap
10        for (auto &row : grid) {
11            for (int x : row) {
12                total += x;
13                bottomMap[x]++;
14                rightMap[x]++;
15            }
16        }
17
18        long long sumTop = 0;
19
20        // Horizontal cuts
21        for (int i = 0; i < m - 1; i++) {
22            for (int j = 0; j < n; j++) {
23                int val = grid[i][j];
24                sumTop += val;
25
26                topMap[val]++;
27                bottomMap[val]--;
28            }
29
30            long long sumBottom = total - sumTop;
31
32            if (sumTop == sumBottom) return true;
33
34            long long diff = abs(sumTop - sumBottom);
35
36            if (sumTop > sumBottom) {
37                if (check(topMap, grid, 0, i, 0, n-1, diff)) return true;
38            } else {
39                if (check(bottomMap, grid, i+1, m-1, 0, n-1, diff)) return true;
40            }
41        }
42
43        long long sumLeft = 0;
44        for (int j = 0; j < n - 1; j++) {
45            for (int i = 0; i < m; i++) {
46                int val = grid[i][j];
47                sumLeft += val;
48
49                leftMap[val]++;
50                rightMap[val]--;
51            }
52
53            long long sumRight = total - sumLeft;
54            if (sumLeft == sumRight) return true;
55
56            long long diff = abs(sumLeft - sumRight);
57
58            if (sumLeft > sumRight) {
59                if (check(leftMap, grid, 0, m-1, 0, j, diff)) return true;
60            } else {
61                if (check(rightMap, grid, 0, m-1, j+1, n-1, diff)) return true;
62            }
63        }
64
65        return false;
66    }
67
68    bool check(unordered_map<long long,int>& mp, vector<vector<int>>& grid,
69           int r1, int r2, int c1, int c2, long long diff) {
70
71        int rows = r2 - r1 + 1;
72        int cols = c2 - c1 + 1;
73
74        // single cell
75        if (rows * cols == 1) return false;
76
77        // 1D row
78        if (rows == 1) {
79            return (grid[r1][c1] == diff || grid[r1][c2] == diff);
80        }
81
82        // 1D column
83        if (cols == 1) {
84            return (grid[r1][c1] == diff || grid[r2][c1] == diff);
85        }
86
87        return mp[diff]>0;
88    }
89};