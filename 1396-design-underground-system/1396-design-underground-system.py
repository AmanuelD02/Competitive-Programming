class UndergroundSystem:

    def __init__(self):
        self.avg = {}
        self.checkedIn = {}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedIn[id] = (stationName, t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkedIn[id]
        oldAvg = (0,0) if not (startStation, stationName) in self.avg else self.avg[(startStation, stationName)]
        self.avg[(startStation, stationName)] = (oldAvg[0] + (t- startTime), oldAvg[1] + 1)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.avg[(startStation, endStation)]
        return total/ count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)