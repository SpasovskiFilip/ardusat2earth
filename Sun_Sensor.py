import cv2
import math
import cv2 as cv
im_grey = cv2.imread('C:\\Users\\Nikola\\Desktop\\pic3.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)

img=cv2.imread('C:\\Users\\Nikola\\Desktop\\pic3.jpg')
im_grey=cv2.GaussianBlur(im_grey,(61,61),200)
q=0
m=0
n=0
p=[0,0]
for i in range(0,421):
    for j in range(0,639):
        if im_grey[i,j]>q:
            q=im_grey[i,j]
            #print q,"\t",m,"\t",n
            m=i
            n=j

p[0]=-m+211
p[1]=n-320
print p
pitch=(float(p[0]/422.0))*140
yaw=float(p[1]/640.0)*180
print pitch
print yaw
print float(p[0]/422.0)

cv2.imwrite('C:\\Users\\Nikola\\Desktop\\pic_blurred.jpg', im_grey)


#print im_gray.item(0,0)
#print math.atan()
