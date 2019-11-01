STD_POS = [
    [0, 0],         # 좌하
    [1000, 0],      # 우하
    [1000, 1000],   # 우상
    [0, 1000]       # 좌상
]
MAXIMUM_NEXT_DISTANCE = 100
POS_GAP = 50
flyTo = 0
STD_POS[0][0] -= POS_GAP

nowX, nowY = STD_POS[0]

targetList = []
targetList.append([nowX, nowY])

while True:
    # 좌하에서 우하
    if flyTo == 0:
        nowX += MAXIMUM_NEXT_DISTANCE
        if nowX >= STD_POS[1][0]:
            nowX = STD_POS[1][0]
            flyTo = 1
            STD_POS[0][0] += POS_GAP
            STD_POS[0][1] += POS_GAP
        
        targetList.append([nowX, nowY])

        if STD_POS[0][0] >= STD_POS[2][0]:
            break
        if STD_POS[0][1] >= STD_POS[2][1]:
            break
    # 우하에서 우상
    elif flyTo == 1:
        nowY += MAXIMUM_NEXT_DISTANCE
        if nowY >= STD_POS[2][1]:
            nowY = STD_POS[2][1]
            flyTo = 2
            STD_POS[1][0] -= POS_GAP 
            STD_POS[1][1] += POS_GAP 
        
        targetList.append([nowX, nowY])

        if STD_POS[1][0] <= STD_POS[3][0]:
            break
        if STD_POS[1][1] >= STD_POS[3][1]:
            break
    # 우상에서 좌상
    elif flyTo == 2:
        nowX -= MAXIMUM_NEXT_DISTANCE
        if nowX <= STD_POS[3][0]:
            nowX = STD_POS[3][0]
            flyTo = 3
            STD_POS[2][0] -= POS_GAP 
            STD_POS[2][1] -= POS_GAP 
        
        targetList.append([nowX, nowY])

        if STD_POS[2][0] <= STD_POS[0][0]:
            break
        if STD_POS[2][1] <= STD_POS[0][1]:
            break
    # 좌상에서 좌하
    elif flyTo == 3:
        nowY -= MAXIMUM_NEXT_DISTANCE
        if nowY <= STD_POS[0][1]:
            nowY = STD_POS[0][1]
            flyTo = 0
            STD_POS[3][0] += POS_GAP 
            STD_POS[3][1] -= POS_GAP 
        
        targetList.append([nowX, nowY])

        if STD_POS[3][0] >= STD_POS[1][0]:
            break
        if STD_POS[3][1] <= STD_POS[1][1]:
            break

print(targetList)


