a, b = list(map(int, input().split()))
queue = list(input())


for _ in range(b):
    i = 1
    while i < len(queue):
        if queue[i] == 'G':
            queue[i-1], queue[i] =  queue[i],  queue[i-1]
            i += 1
        i += 1


print("".join(queue))