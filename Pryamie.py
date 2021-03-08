import matplotlib.pyplot as plt
import json

with open('image_hough_test.json', 'r') as f:
    image = json.load(f) 

i=0
j=0
b=0
k=0
n=len(image)
m=len(image[0])
points=[]
s=""
ksbs=[]
maxb=0
maxk=0
mink=0
minb=0
for i in range(n):
    for j in range(m):
        if(image[i][j]==1):
            points.append([i,j])

for i in range(len(points)):
    for j in range(i+1,len(points),1):
        if(points[i][0]-points[j][0]!=0):
            k=round((points[i][1]-points[j][1])/(points[i][0]-points[j][0]),2)
            b=round((points[j][1]*points[i][0]-points[i][1]*points[j][0])/(points[i][0]-points[j][0]),2)
            #print(k," ",b)
            if b>maxb:
                maxb=b
            if k>maxk:
                maxk=k
            if k<mink:
                mink=k
            if b<minb:
                minb=b
            ksbs.append([k,b])

s=""
targets={}
for i in range(len(ksbs)):
    s=str(ksbs[i][0])+" "+str(ksbs[i][1])
    if(s in targets):
        targets[s]=targets[s]+1
    else:
        targets[s]=1


#for i in range(len(ksbs)):
    #print(ksbs[i][0]+abs(mink)," ",ksbs[i][1]+abs(minb)," ",n," ",m," ",len(image1)," ",len(image1[0]))
    #image1[ksbs[i][0]+abs(mink)][ksbs[i][1]+abs(minb)]=image1[ksbs[i][0]+abs(mink)][ksbs[i][1]+abs(minb)]+0.1
maxx=0.0
for i in targets:
    if maxx<targets[i]:
        maxx=targets[i]

targets1={}
for i in targets:
    if(targets[i]>=80):
        r=i.split()
        print("y=",r[0],"*x+(",r[1],")")
        targets1[i]=targets[i]


max=[]
x=0
y=0
image2= [[0] * m for i in range (n)]


for i in targets1:
    kl=i.split()
    for x in range(320):
        y=round(float(kl[0])*x+float(kl[1]))
        if(x>=0 and x<len(image2) and y>=0 and y<len(image2[0])):
            image2[x][y]=1

plt.imshow(image2)
plt.show()
plt.imshow(image)
plt.show()