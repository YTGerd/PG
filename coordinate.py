import numpy as po
import numpy.linalg as lg

def getCoordinate (*F):
    A=po.array([[2*(F[0]-F[4]),2*(F[1]-F[5]),2*(F[2]-F[6])],[2*(F[0]-F[8]),2*(F[1]-F[9]),2*(F[2]-F[10])],[2*(F[0]-F[12]),2*(F[1]-F[13]),2*(F[2]-F[14])]])
    B=po.array([[(F[7])**2-(F[3])**2-(F[4])**2+(F[0])**2-(F[5])**2+(F[1])**2-(F[6])**2+(F[2])**2],[(F[11])**2-(F[3])**2-(F[8])**2+(F[0])**2-(F[9])**2+(F[1])**2-(F[10])**2+(F[2])**2],[(F[15])**2-(F[3])**2-(F[12])**2+(F[0])**2-(F[13])**2+(F[1])**2-(F[14])**2+(F[2])**2]])

# AT=tansposition of matix A
    AT=A.transpose()

# d=AT*A
    d=AT.dot(A)

#e=inverse of matrix d
    e=lg.pinv(d)
    f=e.dot(AT)

# X=(AT*A)^-1*AT*B
    X=f.dot(B)
    return X

d1,d2,d3,d4,d5=map(float,input("please input distances d1-d5:").split())

x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,x5,y5,z5=0,1.5,2,2.5,0,2,5,1.5,2,2.5,3,2,2.5,1.5,1.25
H1234=getCoordinate(x1,y1,z1,d1,x2,y2,z2,d2,x3,y3,z3,d3,x4,y4,z4,d4)
H1235=getCoordinate(x1,y1,z1,d1,x2,y2,z2,d2,x3,y3,z3,d3,x5,y5,z5,d5)
H1245=getCoordinate(x1,y1,z1,d1,x2,y2,z2,d2,x4,y4,z4,d4,x5,y5,z5,d5)
H1345=getCoordinate(x1,y1,z1,d1,x3,y3,z3,d3,x4,y4,z4,d4,x5,y5,z5,d5)
H2345=getCoordinate(x2,y2,z2,d2,x3,y2,z3,d3,x4,y4,z4,d4,x5,y5,z5,d5)



def getWeight(h1,h2,h3,x11,y11,z11,x22,y22,z22,x33,y33,z33,x44,y44,z44):
    
    d11=pow((h1-x11)**2+(h2-y11)**2+(h3-z11)**2,0.5)
    d22=pow((h1-x22)**2+(h2-y22)**2+(h3-z22)**2,0.5)
    d33=pow((h1-x33)**2+(h2-y33)**2+(h3-z33)**2,0.5)
    d44=pow((h1-x44)**2+(h2-y44)**2+(h3-z44)**2,0.5)


    Weight=1/(d11+d22+d33+d44)

    return Weight


w1=getWeight(H1234[0,0],H1234[1,0],H1234[2,0],x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4)
w2=getWeight(H1235[0,0],H1235[1,0],H1235[2,0],x1,y1,z1,x2,y2,z2,x3,y3,z3,x5,y5,z5)
w3=getWeight(H1245[0,0],H1245[1,0],H1245[2,0],x1,y1,z1,x2,y2,z2,x4,y4,z4,x5,y5,z5)
w4=getWeight(H1345[0,0],H1345[1,0],H1345[2,0],x1,y1,z1,x3,y3,z3,x4,y4,z4,x5,y5,z5)
w5=getWeight(H2345[0,0],H2345[1,0],H2345[2,0],x2,y2,z2,x3,y3,z3,x4,y4,z4,x5,y5,z5)


C=(H1234*w1+H1235*w2+H1245*w3+H1345*w4+H2345*w5)/(w1+w2+w3+w4+w5)

print(C)

