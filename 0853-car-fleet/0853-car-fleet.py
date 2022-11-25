class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position, speed))
        
        for i in range(len(cars) - 1, -1, -1):
            cur_car = cars[i]
            time = (target - cur_car[0]) / cur_car[1]
            if stack:
                next_car = cars[stack[-1]]
                next_time = (target - next_car[0]) / next_car[1]
                
                if next_time < time:
                    stack.append(i)
                    
            else:
                stack.append(i)
        
        return len(stack)