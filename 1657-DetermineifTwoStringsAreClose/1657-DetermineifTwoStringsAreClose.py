# Last updated: 30/08/2026, 20:02:15
1class Solution:
2    def closeStrings(self, word1: str, word2: str) -> bool:
3        # 1. If lengths are different, they can never be close
4        if len(word1) != len(word2):
5            return False
6            
7        wordone = {}
8        wordtwo = {}
9        
10        # 2. Correctly count characters for word1
11        for x in word1:
12            wordone[x] = wordone.get(x, 0) + 1
13            
14        # 3. Correctly count characters for word2
15        for y in word2:
16            wordtwo[y] = wordtwo.get(y, 0) + 1
17            
18        # 4. Check Operation 1: Both words must have the exact same unique characters
19        if set(wordone.keys()) != set(wordtwo.keys()):
20            return False
21
22            
23        # 5. Check Operation 2: Both words must have the same collection of frequencies
24        return sorted(wordone.values()) == sorted(wordtwo.values())
25