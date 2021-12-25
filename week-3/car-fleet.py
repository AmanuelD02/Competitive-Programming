from typing import *
def carFleet( target: int, position: List[int], speed: List[int]) -> int:
    stack = []
    cars = list(map(lambda x, y:(x,y), position, speed))
    cars.sort()
    print("cars", cars)
    speeds = []
    for car in cars:
        speeds.append((target- car[0])/car[1])

    print("speeds",speeds)
    for car in speeds:
        while stack and stack[-1] <= car:
            stack.pop()
        stack.append(car)
    print("stack",stack)

    return len(cars)


        


carFleet(12,  [10,10,10],  [2,2,2])
# carFleet(100,  [0,2,4],  [4,2,1])

    