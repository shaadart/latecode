class Solution(object):
    def mergeAlternately(self, word1, word2):
        i,j = 0,0
        merged = []
        while i < len(word1) and j < len(word2):
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1

        if i < len(word1):
            merged.append(word1[i:])
        if j < len(word2):
            merged.append(word2[j:])

        return "".join(merged)
