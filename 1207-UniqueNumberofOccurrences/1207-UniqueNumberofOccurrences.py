# Last updated: 30/08/2026, 18:55:11
1class Solution:
2    def uniqueOccurrences(self, arr: List[int]) -> bool:
3        # Step 1: Count the frequency of each number using a standard dictionary
4        counts = {}
5        for num in arr:
6            counts[num] = counts.get(num, 0) + 1
7            
8        # Step 2: Extract the frequencies
9        frequencies = counts.values()
10        print(counts)
11        print(frequencies)
12        print(len(frequencies))
13        print(len(set(frequencies)))
14
15        
16        # Step 3: Check if the frequencies are unique
17        return len(frequencies) == len(set(frequencies))
18