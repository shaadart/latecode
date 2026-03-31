class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        N = n + m - 1 

        word = ['#'] * N
        can_change = [False] * N

        #Processing te T:

        for i in range(n):
            if str1[i] == "T":
                for j in range(m):
                    if word[i+j] != '#' and word[i+j] != str2[j]:
                        return ""

                    word[i+j] = str2[j]   

        # filling a

        for i in range(N):
            if word[i] == "#":
                word[i] = 'a'
                can_change[i] = True

        #helper function
        def is_same(i):
            return word[i:i+m] == list(str2)

        # Processfigng F

        for i in range(n):
            if str1[i] == "F":
                if is_same(i):
                    changed = False

                    for k in range(i+m-1, i-1, -1): 
                        
                        #reading it backwards bcs we need to find lexicographically smallest output so changing staring ones we will mess the shit up 

                        if can_change[k]:
                            word[k] = "b"
                            changed = True
                            break

                    if not changed:
                        return ""

        return "".join(word)