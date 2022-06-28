class Solution:
    def minDeletions(self, s: str) -> int:
        freq = sorted([x[1] for x in Counter(s).items()])
        minVal = float("inf")
        total = 0
        for num in reversed(freq):
            if minVal <= num:
                # print(num , minVal)
                total += (num - minVal + 1)
                minVal -= 1
                minVal = max(1, minVal)
            else:
                minVal = num
        return total
            