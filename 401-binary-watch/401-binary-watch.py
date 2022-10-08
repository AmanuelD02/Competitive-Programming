class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        nums = {1:"01",2:"02",3:"03",4:"04",5:"05",6:"06",7:"07",8:"08",9:"09",0:"00"}
        
        picked = ["0"]*10
        ans = []
        
        def valid(picked, left):
            if left > 0: return False
            if int("".join(picked[:4]), 2) > 11: return False
            if int("".join(picked[4:]), 2) > 59: return False
            
            return True
        def recur(i, left, picked):
            if i >= len(picked) or left == 0:
                if valid(picked,left):
                    ans.append(picked[:])
                return
            
            
            for ch in range(2):
                init = picked[i]
                picked[i] = str(ch)
                if ch == 1: left -= 1
                recur(i+1,left,picked)
                picked[i] = init
        
        
        recur(0,turnedOn, picked)
        # print(ans)
        def changeListToTime(lst):
            hour, mins = int("".join(lst[:4]),2), int("".join(lst[4:]),2)

            hour = str(hour)
            mins = str(mins) if mins > 9 else nums[mins]
            return hour + ":" + mins
            
        return [changeListToTime(lst) for lst in ans]
        