def merge(arr):
    if len(arr)==1:
        return arr
    
    mid = len(arr)//2
    
    return merger(merge(arr[:mid]),merge(arr[mid:]))

def merger(arr1,arr2):
    n = len(arr1)
    m = len(arr2)
    arr = []
    j= i = 0
    while(i<n and j<m):
        if int(arr1[i]) > int(arr2[j]):
            arr.append(arr2[j])
            j+=1
        else:
            arr.append(arr1[i])
            i+=1
    while(i<n):
        arr.append(arr1[i])
        i+=1
    while(j<m):
        arr.append(arr2[j])
        j+=1
    return arr
    