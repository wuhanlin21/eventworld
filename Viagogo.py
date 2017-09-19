
# coding: utf-8

import numpy as np
import random
import decimal
import operator
class world(object):
    def __init__(self, xsize, ysize):
        self.world = {}
        self.xsize = xsize
        self.ysize = ysize
        
    def creatCordinate(self):
        for x in range(-self.xsize,self.xsize+1):
            for y in range(-self.ysize,self.ysize+1):
                corTuple = (x,y)
                self.world[corTuple] = []
                
    def creatEvent(self, n):
        self.eventIdList = range(1,n+1)
        self.visited = []
        for i in self.eventIdList:
            rep = 1
            while rep: 
                x = random.randint(-self.xsize,self.xsize)
                y = random.randint(-self.ysize,self.ysize)
                corTuple = (x,y)
                if corTuple not in self.visited:
                    tempDict = {}
                    tempDict['eventId'] = i
                    priceNumber = random.randint(1,5)
                    priceList = []
                    for p in range(priceNumber):
                        priceList.append("{0:.2f}".format(float(decimal.Decimal(random.randrange(1, 9999))/100)))
                    tempDict['priceList'] = priceList
                    self.world[corTuple].append(tempDict)
                    self.visited.append(corTuple)
                    rep = 0
                    
    def getCloseCord(self, newCord):
        distDict = {}
        if newCord[0]<-10 or newCord[1]<-10 or newCord[0]>10 or newCord[1]>10:
            raise Exception("Invalid Coordinates!")
        for (x,y) in self.visited:
            dist = abs(x-newCord[0])+abs(y-newCord[1])
            distDict[(x,y)] = dist
        if len(self.eventIdList)>5:
            closest = sorted(distDict.items(), key=operator.itemgetter(1))[:5]
        else:
            closest = sorted(distDict.items(), key=operator.itemgetter(1))
        return closest
    
    
    def getEvent(self, newCord):
        closeEventList = []
        try:
            closest = self.getCloseCord(newCord)
        except Exception as e:
            print e
            return 
        for (i,dist) in closest:
            cord = i
            eventId = self.world[cord][0]['eventId']
            priceLow = min(self.world[cord][0]['priceList'])
            eventStr = "Event "+str(eventId).zfill(3)+" - " +"$"+str(priceLow).zfill(5)+", "+"Distance "+str(dist)
            closeEventList.append(eventStr)
        print "Closest Events to "+str(newCord)+":"
        for es in closeEventList:
            print es
            
            
if __name__ == "__main__":
    Testworld = world(10,10)
    Testworld.creatCordinate()
    Testworld.creatEvent(5) # 5 is the number of total events
    ri = raw_input("Please Input Coordinates:\n").split(",")
    newCord = (int(ri[0]),int(ri[1]))
    Testworld.getEvent(newCord)


    
    
                    

        
        
            
    
    

