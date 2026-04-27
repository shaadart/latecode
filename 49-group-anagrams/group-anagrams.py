class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        out = []
        sortedstrs = strs[:]

        #sort
        for i in range(len(strs)):
            sortedstrs[i] = "".join(sorted(strs[i]))

        
        # for i in range(len(sortedstrs)):
        #     for j in range():
        #     if sortedstrs[i] == sortedstrs[i-1]:
        
        groups = defaultdict(list)

        for i in range(len(strs)):
            groups[sortedstrs[i]].append(strs[i])


        for key in groups:
            out.append(groups[key])

        return out

                

        