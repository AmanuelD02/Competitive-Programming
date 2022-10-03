class Solution:
    def minSteps(self, target: int) -> int:
        @lru_cache()
        def recur(curState, prevState):
            if curState > target:
                return float("inf")
            if curState == target:
                return 0

            choice_1 = float("inf")
            if prevState != None:
                choice_1 = 1 + recur(curState + prevState, prevState)
            choice_2 = 2 + recur(2*curState, curState)



            return min(choice_1, choice_2)

        return recur(1,None)