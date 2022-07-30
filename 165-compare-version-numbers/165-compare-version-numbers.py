class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        str1 = version1.split(".")
        str2 = version2.split(".")
        L1, L2 = len(str1), len(str2)
        index = min(L1, L2)
        for i in range(index):
            if int(str1[i]) > int(str2[i]):
                return 1
            if int(str1[i]) < int(str2[i]):
                return -1
        left = str1 if L1 > L2 else str2
        for i in range(index, len(left)):
            if int(left[i]) != 0 :
                return 1 if left == str1 else -1

        
        
        return 0
        