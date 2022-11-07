class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        curWidth = 0
        for i, char in enumerate(s):
            curWidth += widths[ord(char) - ord('a')]
            if curWidth > 100:
                lines +=1
                curWidth = widths[ord(char) - ord('a')]
        
        return [lines, curWidth]