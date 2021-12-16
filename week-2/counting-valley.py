def countingValleys(steps, path):
    # Write your code here
    level = 0
    valley = 0
    for p in path:
        if p == "U":
            level += 1
            if level ==0:
                valley +=1
        else:
            level -= 1
        
    return valley