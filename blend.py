img1= cv2.resize(img1,(1200,1200)) # must be done with equal size images
img2= cv2.resize(img2,(1200,1200))
blended = cv2.addWeited(src1=img1, alpha =0.5 , src2= img2 , beta=0.5, gamma=0) # mixture two images togeher ..increasing alpha values and
#decreasing betal value will result in first image being more visible 
cv2.imshow("output",blended) # show result

#if images are not same 
# topping a small image on top of a larger image
img2= cv2.resize(img2,(600,600))

large_image = img1
smaller_image = img2

x_offset =0 #where the image starts
y_offset =0 

x_end = x_offset + smaller_image.shape[1]
y_end = y_offset + smaller_image[0]

large_image[y_offset:y_end, x_offset:x_end]= smaller_image #puts the small image on starting side of the large image

cv2.imshow("out",large_image)
