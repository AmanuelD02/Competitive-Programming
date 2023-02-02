class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit, ans = [], []

        for log in logs:
            if log.split()[1].isdigit():
                digit.append(log)
            else:
                ans.append(log)
        
        def comparator(log):
            return [log.split(" ")[1:], log.split(" ")[0]]
    
        return sorted(ans, key = comparator)  + digit