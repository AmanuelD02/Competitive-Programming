

# def twoStacks(maxSum, a, b):
#     # Write your code here
    
#     a.reverse()
#     b.reverse()
    
#     totalSum = 0
#     count = 0
#     print(a,b)
#     while totalSum < maxSum and a != []  and b!=[]:
#         theMin = min(a[-1], b[-1])
        
#         if theMin == a[-1]:
#             totalSum += a.pop()
#             print("a", a, b)
#             if totalSum >maxSum:
#                 print(count)
#                 return count
#             count +=1
#         elif theMin == b[-1]:
#             totalSum += b.pop()
#             print("b", a,b)
#             if totalSum > maxSum:
#                 print(count)
#                 return count
#             count +=1
    
#     while a !=[]:
#         totalSum += a.pop()
#         print("aa", a,b)
#         if totalSum > maxSum:
#             print(count)
#             return count
#         count +=1
#     while b !=[]:
#         totalSum +=b.pop()
#         print("bb", a,b)
#         if totalSum > maxSum:
#             print(count)
#             return count
#         count +=1
#     print(count)
#     return count



# # twoStacks(100, [4, 2, 4, 6,1], [2, 1, 8, 5])
# twoStacks(10, [9,2,3,4,9], [9,7,7,9])


# def twoStacks(maxSum, a, b):

#     totalSum = 0
#     count = 0
#     l1 = l2 = 0
#     a.reverse()
#     b.reverse()

#     def dfs(totalSum,l1,l2):
#         if l1 < 0:
#             totalSum += b[l2]
#             if totalSum < maxSum:
#                 dfs(totalSum, l1, )