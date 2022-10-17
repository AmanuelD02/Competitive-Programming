class Solution:
    def canMeasureWater(self, j1: int, j2: int, target: int) -> bool:
        """
        # ADD TO J1
        # ADD TO J2
        # REMOVE FROM J1
        # REMOVE FROM J2
        # ADD FROM J1 TO J2
        # ADD FROM J2 TO J1
        """
        if j1 + j2 < target: return False
        def validate_state(curJ1, curJ2):
            if curJ1 + curJ2 == target:
                return True
            return curJ1 == target or curJ2 == target
        
        queue, visited = deque([(0,0)]), {(0,0)}
        while queue:
            curJ1, curJ2 = queue.popleft()
            if validate_state(curJ1, curJ2):
                return True
            
            # ADD TO J1
            if (j1, curJ2) not in visited:
                visited.add((j1, curJ2))
                queue.append((j1,curJ2))
                
            # ADD TO J2
            if (curJ1, j2) not in visited:
                visited.add((curJ1, j2))
                queue.append((curJ1, j2))
                
            # REMOVE FROM J1
            if (0, curJ2) not in visited:
                visited.add((0, curJ2))
                queue.append((0, curJ2))
                
            # REMOVE FROM J2
            if (curJ1, 0) not in visited:
                visited.add((curJ1, 0))
                queue.append((curJ1, 0))
            
            # POUR FROM J1 to J2
            nextJ1, nextJ2 = max(0, curJ2 + curJ1 - j2) ,min(j2, curJ2 + curJ1)
            if ( nextJ1 , nextJ2) not in visited:
                visited.add((nextJ1 , nextJ2))
                queue.append((nextJ1 , nextJ2))
            
            # POUR FROM J2 TO J1
            nextJ1, nextJ2 = min(j1,curJ2 + curJ1), max(0, curJ2 + curJ1 - j1)
            if (nextJ1, nextJ2) not in visited:
                visited.add((nextJ1, nextJ2))
                queue.append((nextJ1, nextJ2))
        return False
    
