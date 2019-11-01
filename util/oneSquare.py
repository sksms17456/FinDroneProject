class square:
    def __init__(self):
        self.targetList = []

    def makeRoute(self, route, center, diff):
        if len(route) == 0:
            self.targetList.append([center[0] - diff, center[1] - diff])
            self.targetList.append([center[0] + diff, center[1] - diff])
            self.targetList.append([center[0] + diff, center[1] + diff])
            self.targetList.append([center[0] - diff, center[1] + diff])
        else:
            if not (route[0][0] < center[0] and route[1][0] > center[0] and 
                    route[1][1] < center[1] and route[2][1] > center[1]):
                self.targetList = []
                self.targetList.append([center[0] - diff, center[1] - diff])
                self.targetList.append([center[0] + diff, center[1] - diff])
                self.targetList.append([center[0] + diff, center[1] + diff])
                self.targetList.append([center[0] - diff, center[1] + diff])
        
        return self
        
    def getRoute(self):
        return self.targetList, len(self.targetList)