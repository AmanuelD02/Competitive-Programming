class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        intervals = []
        N = len(s)
        inBound = lambda left, right: 0 <= left <= right < N


        for i in range(N):
            # ODD length palindromes
            left = right = i
            while inBound(left, right) and s[left] == s[right]:
                if (right - left + 1) >= k:
                    intervals.append([left, right + 1])
                right += 1
                left -= 1

            # EVEN length palindromes
            left = i
            right = i + 1
            while inBound(left, right) and s[left] == s[right]:
                if (right - left + 1) >= k:
                    intervals.append([left, right + 1])

                right += 1
                left -= 1
        

        answer = self.maximum_non_overlapping_interval(intervals)

        return answer
    

    def maximum_non_overlapping_interval(self, intervals):
        ans = 0
        last = -inf
        # intervals.sort()
        for x, y in intervals:
            if x >= last:
                last = y
                ans += 1
            else:
                if y < last: last = y
        return ans