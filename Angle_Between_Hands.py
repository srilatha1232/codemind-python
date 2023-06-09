
a=input()
h=(ord(a[0])-48)*10+(ord(a[1])-48)
m=(ord(a[3])-48)*10+(ord(a[4])-48)
if m%2==0:
    angle=30*h-((11*m*1.0)//2)
    if angle<0:
        angle+=360
    if angle>180:
        angle=360-angle
    print("{:.1f}".format(angle))
else:
    angle=(30*h*1.0)-(11*m*1.0/2)
    if angle<0:
        angle+=360
    if angle>180:
        angle=360-angle
    print("{:.1f}".format(angle))    

