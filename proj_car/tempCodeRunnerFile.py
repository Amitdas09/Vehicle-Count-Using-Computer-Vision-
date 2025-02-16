import cv2
import numpy as np

#Web capture
cap=cv2.VideoCapture('video.mp4')
#allowable error between pixel
offset=6
counter=0
#drawing a circle
def center_handel(x,y,w,h):
    x1=int(w/2)
    y1=int(h/2)
    cx=x+x1
    cy=y+y1
    return cx,cy
detect=[]

#initializeing
algo=cv2.bgsegm.createBackgroundSubtractorMOG()#this fun or algo removes the background which shold not be detected

#making a line
line_pos=550

#min width and height of rectangle
min_w=80
min_h=80

while True:
    ret,frame=cap.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(grey,(3,3),5)
    
    #applying on each frame
    img_sub=algo.apply(blur)
    dilat=cv2.dilate(img_sub,np.ones((5,5)))
    kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    dilatada=cv2.morphologyEx(dilat,cv2.MORPH_CLOSE,kernel)
    dilatada=cv2.morphologyEx(dilatada,cv2.MORPH_CLOSE,kernel)
    countershape,h=cv2.findContours(dilatada,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


    #drawline
    cv2.line(frame,(20,line_pos),(1500,line_pos),(0,0,225),thickness=2)

    #draw rectangle
    for (i,c) in enumerate(countershape):
        (x,y,w,h)=cv2.boundingRect(c)
        val=(w>=min_w) and (h>=min_h)
        if not val:
            continue
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
        cv2.putText(frame,"vehicle"+str(counter),(x,y-20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    
        center=center_handel(x,y,w,h)
        detect.append(center)
        cv2.circle(frame,center,4,(0,0,255),-1)

        for (x,y) in detect:
            if y<(line_pos+offset) and y>(line_pos-offset):
                counter+=1
                cv2.line(frame,(20,line_pos),(1200,line_pos),(0,127,255),thickness=2)
                detect.remove((x,y))
                print("car counter :"+str(counter))

    cv2.putText(frame,"vehicle counter :"+str(counter),(200,70),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),3)
    


    cv2.imshow("Output",frame)

    
    if cv2.waitKey(1)==13:
        break
cv2.destroyAllWindows()
cap.release()

