class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Step 1: Count the frequency of each number using a standard dictionary
        counts = {}
        for num in arr:
            counts[num] = counts.get(num, 0) + 1
            
        # Step 2: Extract the frequencies
        frequencies = counts.values()
        print(counts)
        print(frequencies)
        print(len(frequencies))
        print(len(set(frequencies)))

        
        # Step 3: Check if the frequencies are unique
        return len(frequencies) == len(set(frequencies))
