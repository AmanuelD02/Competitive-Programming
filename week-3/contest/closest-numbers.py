import math

# def closestNumbers(arr):
#     import math
#     # Write your code here
#     arr.sort()
#     print(arr)
#     solutions = []
#     minimum = float("inf")
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if i==j:
#                 continue

#             difs = math.fabs(arr[i] - arr[j])
#             if difs> minimum:
#                 continue
#             elif difs == minimum:
#                 solutions.append(arr[i])
#                 solutions.append(arr[j])
#             else:
#                 minimum = difs
#                 solutions = [arr[i], arr[j]]
# #     print(solutions)
#     return solutions
    

def closestNumbers(arr):
    arr.sort()
    solutions = []
    print(arr)
    minimum = float("inf")
    for i in range(len(arr)-1):
        # check ategebun
        difs = math.fabs(arr[i] - arr[i+1])
        if difs <minimum:
            solutions = [arr[i], arr[i+1]]
            minimum = difs
            continue
        j = len(arr) -1

        if difs == minimum:
            solutions.append(arr[i])
            solutions.append(arr[i+1])
            continue
        dif1 = math.fabs(arr[i] - arr[j])
        
        while j >i:
            difs = math.fabs(arr[i] - arr[j])
            if difs < minimum:
                solutions = [arr[i], arr[j]]
                minimum = difs
                continue
            elif difs == minimum:
                solutions.append(arr[i])
                solutions.append(arr[j])
            
            print(j)
            if dif1 < difs:
                break

            j-=1
    print(solutions)
    return solutions


            







# closestNumbers([-520, -470, -20, 30])
# closestNumbers([5 ,4 ,3 ,2])
closestNumbers([-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854, -520, -470])