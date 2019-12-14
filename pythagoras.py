import math
#current coordinates from gps
SX=1
SY=1
FX=6
FY=4
#move distance d
d=2
CX=2
CY=2
#get new coordinates from gps
#cal d1,d2
def dist(a,b,c,d):
    d1=math.sqrt((a-c)**2+(b-d)**2)
    return d1


# d=math.acos(1/2)
#math.degrees(d)
#main
a1=dist(SX,SY,SX,CY)
angle1=math.degrees(math.acos(a1/d))

#big triangle ka angle
print(angle1)
dy1=dist(FX,SY,FX,FY)
dy2=dist(FX,FY,FX,CY)
dx1=dist(FX,FY,SX,FY)
dx2=dist(FX,FY,CX,FY)
angle2=math.degrees(math.atan(dx2/dy2))
print(angle2)
if(dx2>dx1 and dy2<dy1):
    angle=angle1+angle2
    print(angle)
    #rotate bot by angle
elif(dx2>dx1 and dy2>dy1):
    #angle=90+angle1+angle2
    angle=180-angle1+angle2
    print(angle)
elif(dx2 < dx1 and dy2 > dy1):
    #angle=angle2-angle1-90
    angle=angle2+angle1-180
    print(angle) 
elif(dx2 < dx1 and dy2 < dy1):
    angle=angle2-angle1
    print(angle)
    #correct
elif(dx2<dx1 and dy1==dy2):
    angle=angle2-90
    #angle=angle2
    print(angle)
elif(dx2>dx1 and dy1==dy2):
    #angle=angle2+180
    angle=angle2+90
    print(angle)
elif (dx2 == dx1 and dy1>dy2):
    #angle = -angle2
    angle = angle2-180
    print(angle)
elif(dx2 == dx1 and dy1<dy2):
    angle = angle2
    #angle = -(angle2+90)
    print(angle)
else:
    print("check")
    print(angle)
#go forward
#get cordinates MX,MY

#while(MX != Fx && My!=FY):
    #keep moving forward
