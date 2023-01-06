class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = Counter(tasks)
        total = 0
        
        for elem in freq.values():
            if elem % 3 == 0:
                total += elem // 3
            elif elem != 1 and elem % 3 == 1:
                total += ((elem - 4) // 3) + 2

            elif  elem % 3 == 2:
                total += ((elem - 2) // 3) + 1
            else:
                return -1
        
        return total