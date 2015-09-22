__author__ = 'Eugenius'
from PIL import Image
# x=[]
# for i in range(6):
#     for j in range(4):
#         x.append(i*4+j)
#
# for i in range(6):
#     for j in range(4):
#         print x[i*4+j],"  ",
#     print ""
#
# for i in range(6):
#     for j in range(2):
#         print x[(i+1)*4-j-1]

a=Image.open("acorn.jpg").convert("L")
a=a.getdata()
k=[]
for i in range(377):
    for j in range(521,0,-1):
        if  a[i*377+j-1]<195:
            k.append(j)
            break;
print max(k)
