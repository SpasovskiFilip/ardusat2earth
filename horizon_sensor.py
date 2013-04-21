import cv2
import math
import cv2 as cv
im_grey = cv2.imread('C:\\Users\\Nikola\\Desktop\\pic2.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
im_grey=cv2.medianBlur(im_grey,23)
im_grey=cv2.GaussianBlur(im_grey,(3,3),50)

edge = cv2.Canny(im_grey, 200, 0, apertureSize=3)

p1=[0,0]
p2=[0,0]


for i in range(0, 421):
    if(edge[i,0]==255):
        p1=[i,0]
        break

for i in range(0, 421):
        if(edge[i,639]==255):
            p2=[i,639]
            break
        
for i in range(0, 639):
    if(edge[0,i]==255):
        if p1==[0,0]:
            p1=[0,i]
            break
        else:
            p2=[0,i]
            break
if p2==[0,0]:
    for i in range(0, 639):
        if(edge[421,i]==255):
            p2=[421,i]
            break
        
if p1[1]>p2[1]:
    p1,p2=p2,p1

p1[0]=-p1[0]+211
p2[0]=-p2[0]+211
p1[1]=p1[1]-320
p2[1]=p2[1]-320

pitch=-(float(-p1[1]*((p2[0]-p1[0])/(p2[1]-p1[1]))+p1[0])/420)*140
roll=(math.atan(float((p2[0]-p1[0])/(p2[1]-p1[1])))/math.pi)*180


print pitch
print roll


cv2.putText(edge,'PITCH',(20,400),cv2.FONT_HERSHEY_PLAIN,1,(255,255,0))
cv2.putText(edge,str(pitch),(80,400),cv2.FONT_HERSHEY_PLAIN,1,(255,255,0))
cv2.putText(edge,'deg',(240,400),cv2.FONT_HERSHEY_PLAIN,1,(255,255,0))

cv2.putText(edge,'ROLL',(20,370),cv2.FONT_HERSHEY_PLAIN,1,(255,255,0))
cv2.putText(edge,str(roll),(80,370),cv2.FONT_HERSHEY_PLAIN,1,(255,255,0))
cv2.putText(edge,'deg',(150,370),cv2.FONT_HERSHEY_PLAIN,1,(255,255,0))

cv2.imwrite('C:\\Users\\Nikola\\Desktop\\pic1_blurred.jpg', im_grey)  # where Nikola is the name of the folder
cv2.imwrite('C:\\Users\\Nikola\\Desktop\\pic1_new.jpg', edge)         # of the username on the current computer
#print im_gray.item(0,0)
#print math.atan()
print p1,"\t",p2,"\t"
