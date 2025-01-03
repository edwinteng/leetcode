class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        self.travel_time = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        stationPrev,tPrev = self.checkin[id]
        #if (stationPrev,stationName) not in self.travel_time:
        #    self.travel_time[(stationPrev,stationName)] = [t-tPrev]
        #else:
        #    self.travel_time[(stationPrev,stationName)].append(t-tPrev)
        traveltime,numTrip = self.travel_time.get((stationPrev,stationName),(0,0))
        self.travel_time[(stationPrev,stationName)]=(traveltime+t-tPrev,numTrip+1)
        del self.checkin[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totaltime,numTrip = self.travel_time[(startStation,endStation)]
        return totaltime/numTrip
        #timeList = self.travel_time[(startStation,endStation)]
        #return sum(timeList)/len(timeList)

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)