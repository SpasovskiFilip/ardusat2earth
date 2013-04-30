import cv2
import math
import cv2 as cv
img = cv2.imread('C:\\Users\\Nikola\\Desktop\\pic1.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
im_grey=cv2.medianBlur(img,23)
img=cv2.imread('C:\\Users\\Nikola\\Desktop\\pic1.jpg')
im_grey=cv2.GaussianBlur(im_grey,(3,3),50)

edge = cv2.Canny(im_grey, 200, 0, apertureSize=3)
p1=[0,0]
p2=[0,0]
height=len(edge)
width=len(edge[0])
view_angle_x=120
view_angle_y=90

for i in range(0, height-1):
    if(edge[i,0]==255):
        p1=[i,0]
        break

for i in range(0, height-1):
        if(edge[i,width-1]==255):
            p2=[i,width-1]
            break
        
for i in range(0, width-1):
    if(edge[0,i]==255):
        if p1==[0,0]:
            p1=[0,i]
            break
        else:
            p2=[0,i]
            break
if p2==[0,0]:
    for i in range(0, width-1):
        if(edge[height-1,i]==255):
            p2=[height-1,i]
            break
        
if p1[1]>p2[1]:
    p1,p2=p2,p1

p1[0]=-p1[0]+height/2
p2[0]=-p2[0]+height/2
p1[1]=p1[1]-width/2
p2[1]=p2[1]-width/2


k=float(p2[0]-p1[0])/float(p2[1]-p1[1])
b=-p1[1]*k+p1[0]
pitch=-(b/height)*view_angle_y
roll=-(math.atan(k)/math.pi)*180
#print "k=",k
#print "b=",b
print roll
print pitch


for i in range(3,height-1):
    for j in range(3,width):
        if edge[i,j]==255:
            img[i,j]=[0,0,255]
            if ((i<height-3)and(j<width-3)):
                img[i+1,j]=[0,0,255]
                img[i-1,j]=[0,0,255]
                img[i+2,j]=[0,0,255]
                img[i-2,j]=[0,0,255]

cv2.putText(edge,'PITCH',(20,height-20),cv2.FONT_HERSHEY_PLAIN,1,(255,0,255))
cv2.putText(edge,str(pitch),(80,height-20),cv2.FONT_HERSHEY_PLAIN,1,(255,0,255))
cv2.putText(edge,'deg',(240,height-20),cv2.FONT_HERSHEY_PLAIN,1,(255,0,255))

cv2.putText(img,'PITCH',(20,height-20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255))
cv2.putText(img,str(pitch),(80,height-20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255))
cv2.putText(img,'deg',(240,height-20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255))


cv2.putText(edge,'ROLL',(20,height-80),cv2.FONT_HERSHEY_PLAIN,1,(255,0,255))
cv2.putText(edge,str(roll),(80,height-80),cv2.FONT_HERSHEY_PLAIN,1,(255,0,255))
cv2.putText(edge,'deg',(240,height-80),cv2.FONT_HERSHEY_PLAIN,1,(255,0,255))

cv2.putText(img,'ROLL',(20,height-80),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255))
cv2.putText(img,str(roll),(80,height-80),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255))
cv2.putText(img,'deg',(240,height-80),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255))


cv2.imwrite('C:\\Users\\Nikola\\Desktop\\pic_blurred.jpg', im_grey)     # where Nikola is the name of the folder
cv2.imwrite('C:\\Users\\Nikola\\Desktop\\pic_new.jpg', edge)            # of the username on the current computer
cv2.imwrite('C:\\Users\\Nikola\\Desktop\\pic_marked.jpg', img)          

print p1,"\t",p2,"\t"
