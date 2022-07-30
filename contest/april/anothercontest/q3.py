from heapq import heappush, heappop, heapify
minutes = 0
p1, p2 = list(map(int, input().split()))
heap = [p1, p2]
heapify(heap)

while heap:
    # minutes += 1
    charg = heappop(heap)
    disch = heappop(heap)
    if charg <=0 or disch <=0:break
    if charg ==1 and disch ==1: break

    charg +=1
    disch -=2
    minutes +=1
    
    heappush(heap, charg)
    heappush(heap, disch)



print(minutes)


# while heap:
#     # minutes += 1
#     charg = heappop(heap)
#     disch = heappop(heap)
#     if disch <=2:
#         minutes += 1
#         break
#     while disch >2:
#         minutes += 1
#         disch -=2
#         charg +=1
    
#     if charg==1 and disch ==1:
#         # minutes += 1
#         break
#     heappush(heap, charg)
#     heappush(heap, disch)



# print(minutes)
