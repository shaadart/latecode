class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # 1. If lengths are different, they can never be close
        if len(word1) != len(word2):
            return False
            
        wordone = {}
        wordtwo = {}
        
        # 2. Correctly count characters for word1
        for x in word1:
            wordone[x] = wordone.get(x, 0) + 1
            
        # 3. Correctly count characters for word2
        for y in word2:
            wordtwo[y] = wordtwo.get(y, 0) + 1
            
        # 4. Check Operation 1: Both words must have the exact same unique characters
        if set(wordone.keys()) != set(wordtwo.keys()):
            return False

            
        # 5. Check Operation 2: Both words must have the same collection of frequencies
        return sorted(wordone.values()) == sorted(wordtwo.values())
