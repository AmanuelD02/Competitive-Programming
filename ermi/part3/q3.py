hr,min,sec=eval(input())
ehr, emin, esec = eval(input())

start = (hr*3600) + (min*60) + sec
end = (ehr*3600) + (emin*60) + esec

print(end - start)
