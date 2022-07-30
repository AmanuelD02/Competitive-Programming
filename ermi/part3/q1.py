hr,min,sec=eval(input())
elapsed = int(input())

start = (hr*3600) + (min*60) + sec

start += elapsed
newHr = start // 3600
newHr = newHr if newHr < 24 else 0

remaining = start % 3600
newMin = remaining // 60

remaining = remaining %60
newSec = remaining

print(newHr, newMin, newSec)
