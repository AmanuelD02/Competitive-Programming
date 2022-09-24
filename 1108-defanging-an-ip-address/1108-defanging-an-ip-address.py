class Solution:
    def defangIPaddr(self, address: str) -> str:
        stack = []
        defang = '[.]'
        for ad in address:
            if ad =='.':
                stack.append(defang)
            else:
                stack.append(ad)
        return "".join(stack)