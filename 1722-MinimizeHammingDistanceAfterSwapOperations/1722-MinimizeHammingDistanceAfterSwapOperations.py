# Last updated: 4/22/2026, 12:52:15 AM
1class Solution:
2    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
3        n = len(source)
4
5        parent = list(range(n))
6        rank = [0] * n
7
8        def find(x):
9            if parent[x] != x:
10                parent[x] = find(parent[x])
11            return parent[x]
12
13        def unite(a, b):
14            pa, pb = find(a), find(b)
15            if pa == pb:
16                return
17
18            if rank[pa] < rank[pb]:
19                pa, pb = pb, pa
20
21            parent[pb] = pa
22            if rank[pa] == rank[pb]:
23                rank[pa] += 1
24
25        for a, b in allowedSwaps:
26            unite(a, b)
27
28        from collections import defaultdict
29
30        groups = defaultdict(list)
31        for i in range(n):
32            groups[find(i)].append(i)
33
34        ans = 0
35
36        for idxs in groups.values():
37            freq = {}
38
39            for i in idxs:
40                freq[source[i]] = freq.get(source[i], 0) + 1
41
42            for i in idxs:
43                if freq.get(target[i], 0) > 0:
44                    freq[target[i]] -= 1
45                else:
46                    ans += 1
47
48        return ans