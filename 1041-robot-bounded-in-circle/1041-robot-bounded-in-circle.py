class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = y = dx = 0
        dy = 1
        for inst in instructions:
            if inst == 'R':
                dx, dy = dy, -dx
            if inst == 'L':
                dx, dy = -dy, dx
            if inst == 'G':
                x, y = x + dx, y + dy
        

        return (x, y) == (0, 0) or (dx, dy) != (0,1)