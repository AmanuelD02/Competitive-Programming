from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_list = SortedList()
        ans = []
        for num in reversed(nums):
            sorted_list.add(num)
            ans.append(sorted_list.index(num))
        return ans[::-1]