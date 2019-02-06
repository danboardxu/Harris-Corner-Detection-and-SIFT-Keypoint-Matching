import cv2
import numpy as np
import math

def gradientCalculation(image,window_size,k,threshold):    
## Gradient
    dx, dy = np.gradient(image)
    Ixx = dx*dx
    Ixy = dx*dy
    Iyy = dy*dy
##GAUSSIAN BLUR
    Ixx= cv2.GaussianBlur(Ixx,(5,5),0)     
    Iyy = cv2.GaussianBlur(Iyy,(5,5),0)
    Ixy = cv2.GaussianBlur(Ixy,(5,5),0)
    cv2.imshow("dd",Ixy)

    imageHeight,imageWidth=image.shape

    neighbours=np.uint8((window_size-1)/2)
    keypoint=[]
    reg=((Ixx*Iyy)-(Ixy*Ixy))
    trace=Ixx+Iyy
    r2=(reg-(k*trace))
    a,b,c,d=cv2.minMaxLoc(r2)
    r3=np.zeros(image.shape,np.float32)
    r4=np.zeros(image.shape,np.float32)
    print(b)
    
    x1=0
    y1=0
    extra=[]
    for y in range(neighbours, imageHeight-neighbours):
        for x in range(neighbours, imageWidth-neighbours):
                    r = r2[y-neighbours:y+neighbours+1, x-neighbours:x+1+neighbours]
                    a,b,c,d=cv2.minMaxLoc(r)
                    abc=np.zeros((window_size,window_size),np.float32)
                    abc[d]=b
    
                    if b>threshold:
                        r3[y-neighbours:y+neighbours+1, x-neighbours:x+neighbours+1]=abc
                        keypoint.append(cv2.KeyPoint(x,y,1,-1,0,0,-1))                    
                        extra.append(b)
    cv2.imshow("xxxx",r3)
    print(cv2.minMaxLoc(r3))
    img2 =cv2.drawKeypoints(image,keypoint,image,color=(0,255,0), flags=0)
    return r2,r3,img2,image,keypoint 

def main():
    image=cv2.imread("Resources/img.jpg",0)
    image2=cv2.imread("Resources/checkerboard.png",0)
    window_size=9
    k=0.04
    threshold=71595092
    r2,r3,img2,image,keypoints=gradientCalculation(image,window_size,k,threshold)



##    # find Harris corners
##    image = np.float32(image)
##    dst = cv2.cornerHarris(image,2,3,0.04)
##    dst = cv2.dilate(dst,None)
##    ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
##    dst = np.uint8(dst)
##
##    # find centroids
##    ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
##
##    # define the criteria to stop and refine the corners
##    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
##    corners = cv2.cornerSubPix(image,np.float32(centroids),(5,5),(-1,-1),criteria)
##
##
##    img=cv2.imread("Resources/checkerboard-sq.jpg")
##
##
##    # Now draw them
##    res = np.hstack((centroids,corners))
##    res = np.int0(res)
##    img[res[:,1],res[:,0]]=[0,0,255]
##    img[res[:,3],res[:,2]] = [0,255,0]
##
##    cv2.imshow('subpixel5.png',img)






    cv2.imshow("Marks",img2)
    cv2.imwrite("nd.png",img2)









































##    r2x,r3x,img2x,imagex,keypointsx=gradientCalculation(image2,window_size,k,threshold)
##    cv2.imshow("Marks2",img2x)
##    cv2.imwrite("nd2.png",img2x)
##    abc=[]
##    img3 = cv2.drawMatches(img2,keypoints,img2x,keypointsx,(keypoints,keypointsx),None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
##    cv2.imshow("Marks3",img3)


    


main()






















