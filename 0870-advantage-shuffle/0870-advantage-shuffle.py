class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        
        nums1.sort()
        queue = deque(nums1)
        Found = False
        
        for num, i in sorted(zip(nums2, range(n))):
            if num < queue[0]:
                nums2[i] = queue.popleft()
            else:
                if not Found:
                    for j in range(len(queue)):
                        if num >= queue[0]:
                            queue.append(queue.popleft())
                        else:
                            break
                            
                    if j == len(queue):
                        Found = True
                
                nums2[i] = queue.popleft()
        
        return nums2
        