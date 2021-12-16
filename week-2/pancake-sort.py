def pancakeSort(arr):
    def swap(r):
        l=0
        while(r>l):
            print("swap",arr)
            print(l,r)
            arr[l], arr[r] = arr[r], arr[l]
            l+=1
            r-=1
        
    sorted  = arr[:]
    sorted.sort()
    flips = []
    i =0
    print(sorted, arr)
    while( sorted != arr):
        f = arr[i]
        print("swap", i)
        # print(f, i)
        if f-1 == i:
            i+=1
            continue
        else:
            i=0
            # print("ELSE")
            flips.append(f-1)
            swap(f-1)
    print("sorted",flips)
    print(sorted, arr)
    return flips
    
    



pancakeSort([3,2,4,1])
# pancakeSort([1,2,3])