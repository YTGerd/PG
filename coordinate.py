import numpy as po
import numpy.linalg as lg
x1,y1,z1=4,1,3
x2,y2,z2=3,3,5
x3,y3,z3=7,4,3
x4,y4,z4=4,0,0
d1,d2,d3,d4=3,6,2,8

A=po.array([[2*(x1-x2),2*(y1-y2),2*(z1-z2)],[2*(x1-x3),2*(y1-y3),2*(z1-z3)],[2*(x1-x4),2*(y1-y4),2*(z1-z4)]])
B=po.array([[d2**2-d1**2-x2**2+x1**2-y2**2+y1**2-z2**2+z1**2],[d3**2-d1**2-x3**2+x1**2-y3**2+y1**2-z3**2+z1**2],[d4**2-d1**2-x4**2+x1**2-y4**2+y1**2-z4**2+z1**2]])

# AT=tansposition of matix A
AT=A.transpose()

# d=AT*A
d=AT.dot(A)

#e=inverse of matrix d
e=lg.inv(d)
f=e.dot(AT)

# X=(AT*A)^-1*AT*B
X=f.dot(B)
print(X)
