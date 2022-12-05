from collections import deque

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        accessTimes = list(zip(keyName, keyTime))
        accessTimes.sort()
        
        alertedPersons = set()
        
        keyCard = {}
        
        for name, time in accessTimes:
            time = self.changeMins(time)
            if not name in keyCard:
                keyCard[name] = deque()
            
            keyCard[name].append(time)
            
            while len( keyCard[name]) > 1 and time - keyCard[name][0] > 60:
                keyCard[name].popleft()
            
            # print(keyCard)
            if len(keyCard[name]) >= 3:
                alertedPersons.add(name)
        
        
        
        return sorted(list(alertedPersons))

            
    
    
    
    def changeMins(self, time):
        hour, mins = time.split(":")
        return int(hour) * 60 + int(mins)