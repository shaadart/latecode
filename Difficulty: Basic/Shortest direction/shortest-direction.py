class Solution:
    def shortestPath(self, s):
        
        direction = {'E': 0, 'W': 0, 'N': 0, 'S': 0}
        
        for ch in s:
            direction[ch] += 1
            
            
            
        #net vertical and net horizontal 
        vertical = abs(direction['S'] - direction['N'])
        horizontal = abs(direction['W'] - direction['E'])
        
        vsym = "S" if direction["S"] > direction["N"] else "N"
        hsym = "E" if direction["E"] > direction["W"] else "W"
        
        output = []
        #output:
        for i in range(vertical):
            output.append(vsym)
            
        for i in range(horizontal):
            output.append(hsym)
            
        output.sort()
        return "".join(output) 
            
        
        
        
            
            
	        
        