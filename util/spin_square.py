class square:
    def __init__(self, std=[[0, 0], [100, 0], [100, 100], [0, 100]], maximum=10, gap=10):
        self.std = std
        self.max = maximum
        self.gap = gap
    
    def getRoute(self):
        self.std[0][0] -= self.gap
        flyTo = 0

        nowX, nowY = self.std[0]

        targetList = []
        targetList.append([nowX, nowY])

        while True:
            # 좌하에서 우하
            if flyTo == 0:
                nowX += self.max
                if nowX >= self.std[1][0]:
                    nowX = self.std[1][0]
                    flyTo = 1
                    self.std[0][0] += self.gap
                    self.std[0][1] += self.gap
                
                targetList.append([nowX, nowY])

                if self.std[0][0] >= self.std[2][0]:
                    break
                if self.std[0][1] >= self.std[2][1]:
                    break
            # 우하에서 우상
            elif flyTo == 1:
                nowY += self.max
                if nowY >= self.std[2][1]:
                    nowY = self.std[2][1]
                    flyTo = 2
                    self.std[1][0] -= self.gap 
                    self.std[1][1] += self.gap 
                
                targetList.append([nowX, nowY])

                if self.std[1][0] <= self.std[3][0]:
                    break
                if self.std[1][1] >= self.std[3][1]:
                    break
            # 우상에서 좌상
            elif flyTo == 2:
                nowX -= self.max
                if nowX <= self.std[3][0]:
                    nowX = self.std[3][0]
                    flyTo = 3
                    self.std[2][0] -= self.gap 
                    self.std[2][1] -= self.gap 
                
                targetList.append([nowX, nowY])

                if self.std[2][0] <= self.std[0][0]:
                    break
                if self.std[2][1] <= self.std[0][1]:
                    break
            # 좌상에서 좌하
            elif flyTo == 3:
                nowY -= self.max
                if nowY <= self.std[0][1]:
                    nowY = self.std[0][1]
                    flyTo = 0
                    self.std[3][0] += self.gap 
                    self.std[3][1] -= self.gap 
                
                targetList.append([nowX, nowY])

                if self.std[3][0] >= self.std[1][0]:
                    break
                if self.std[3][1] <= self.std[1][1]:
                    break
                    
        return targetList