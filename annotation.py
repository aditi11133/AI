import cv2
import matplotlib.pyplot as plt
image_path='image.jpg'
image=cv2.imread(image_path)
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
height,width,_=image_rgb.shape
recti_width,recti_height=150,150
top_lefti=(20,20)
bottom_righti=(top_lefti[0]+recti_width,top_lefti[1]+recti_height)
cv2.rectangle(image_rgb,top_lefti,bottom_righti,(0,255,255),3)
rect2_width,rect2_height=200,150
top_left2=(width-rect2_width-20,height-rect2_height-20)
bottom_right2=(top_left2[0]+rect2_width,top_left2[1]+rect2_height)
cv2.rectangle(image_rgb,top_left2,bottom_right2,(255,0,255),3)
center1_x=top_lefti[0]+recti_width//2
center1_y=top_lefti[1]+recti_height//2
center2_x=top_left2[0]+rect2_width//2
center2_y=top_left2[1]+rect2_height//2
cv2.circle(image_rgb,(center1_x,center1_y),15,(0,255,0),-1)
cv2.circle(image_rgb,(center2_x,center2_y),15,(0,0,255),-1)
cv2.line=(image_rgb,(center1_x,center1_y),(center2_x,center2_y),(0,255,0),3)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image_rgb,'Region1',(top_lefti[0],top_lefti[1]-10),font,0.7,(0,255,255),2,cv2.LINE_AA)
cv2.putText(image_rgb,'Region2',(top_left2[0],top_left2[1]-10),font,0.7,(255,0,255),2,cv2.LINE_AA)
cv2.putText(image_rgb,'Center1',(center1_x-40,center1_y+40),font,0.7,(0,255,0),2,cv2.LINE_AA)
cv2.putText(image_rgb,'Center2',(center2_x-40,center2_y+40),font,0.7,(0,0,255),2,cv2.LINE_AA)
arrow_start=(width-50,20)
arrow_end=(width-50,height-20)
cv2.arrowedLine(image_rgb,arrow_start,arrow_end,(255,255,0),3,tipLength=0.05)
cv2.arrowedLine(image_rgb,arrow_end,arrow_start,(255,255,0),3,tipLength=0.05)
height_label_position=(arrow_start[0]-150,(arrow_start[1]+arrow_end[1])//2)
cv2.putText(image_rgb,f'Height:{height}px',height_label_position,font,0.8,(255,255,0),2,cv2.LINE_AA)
plt.figure(figsize=(12,0))
plt.imshow(image_rgb)
plt.title("Annotated image")
plt.axis("off")
plt.show()