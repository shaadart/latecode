# Last updated: 3/13/2026, 12:27:22 AM
1class DSU:
2    def __init__(self, n):
3        self.parent = list(range(n))
4        self.groups = n
5
6    def find(self, x):
7        if self.parent[x] != x:
8            self.parent[x] = self.find(self.parent[x])
9        return self.parent[x]
10
11    def unite(self, a, b):
12        pa = self.find(a)
13        pb = self.find(b)
14
15        if pa == pb:
16            return False
17
18        self.parent[pb] = pa
19        self.groups -= 1
20        return True
21
22
23class Solution:
24    def maxStability(self, n, edges, k):
25
26        dsu = DSU(n)
27
28        must_strength = []
29        opt_strength = []
30
31        must_edges = []
32        opt_edges = []
33
34        for e in edges:
35            if e[3] == 1:
36                must_edges.append(e)
37            else:
38                opt_edges.append(e)
39
40        for e in must_edges:
41            if dsu.unite(e[0], e[1]) == False:
42                return -1
43            must_strength.append(e[2])
44
45        opt_edges.sort(key=lambda x: 2*x[2], reverse=True)
46
47        for e in opt_edges:
48            if dsu.unite(e[0], e[1]) == True:
49                opt_strength.append(e[2])
50
51        if dsu.groups > 1:
52            return -1
53
54        opt_strength.sort()
55
56        used = 0
57        for i in range(len(opt_strength)):
58            if used == k:
59                break
60            opt_strength[i] *= 2
61            used += 1
62
63        res = float('inf')
64
65        for v in must_strength:
66            res = min(res, v)
67
68        for v in opt_strength:
69            res = min(res, v)
70
71        return res