import cv2 #import cv2 module
image = cv2.imread("D:/root.tiff") #provide the path of the image
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convert the image into grayscale form 
image = cv2.bitwise_not(image_gray) #inverts the pixel value of the image
blur = cv2.medianBlur(image,5) #use of median blur
ret3, image = cv2.threshold(blur, 0 ,255, cv2.THRESH_BINARY+cv2.THRESH_TRIANGLE) #thresholding of the image using triangle method of thresholding
thinning = cv2.ximgproc.thinning(image) #thinning of the thresholded image using ximgproc thinning function
_, labels = cv2.connectedComponents(thinning, connectivity=8) #use connected component with stat function
num_components, labels, stats, centroids = cv2.connectedComponentsWithStats(thinning) 
length = stats[:, cv2.CC_STAT_AREA]
length = list(sorted(length))
assert len(length) >= 2
total_length = 0
noise = 1 #set the noise threshold for particle clearing in terms of pixels for TRL
for i, length in enumerate(length[:-1]):
    if length > noise:
        total_length += length
        TRL = total_length*0.0063 # conversion of number of pixels into standard value of cm
ret3,th1 = cv2.threshold(image_gray, 170,255,cv2.THRESH_BINARY_INV) # Global thresholding
num_components, labels, stats, centroids = cv2.connectedComponentsWithStats(th1) #use connected component with stat function for area estimation
areas = stats[:, cv2.CC_STAT_AREA]
areas = list(sorted(areas))
assert len(areas) >= 2
total_area = 0
noise_threshold = 250 #set the noise threshold for particle clearing in terms of pixels for PA
for i, area in enumerate(areas[:-1]):
    if area > noise_threshold:
        total_area += area
        PA = total_area/24964 # stores the projected area of the image in cm2 format
SA = PA*3.1415926
AD = PA/TRL
RV = 3.1415926 *(AD/2)**2 * TRL
print(f"Total root length is: {TRL} cm") #print length in cm
print('The root surface area is:', SA, 'cm2') #prints the root surface area
print('The average diameter is:', AD, 'cm') #prints the average diameter of the root 
print('The root volume is:', RV, 'cm3') #prints the root volume
down_points = (1000, 1000)
resized_thinned = cv2.resize(thinning, down_points, interpolation= cv2.INTER_LINEAR)
cv2.imshow('Resized Down by defining height and width', resized_thinned) #display the resized thinned image
cv2.waitKey(0)
cv2.destroyAllWindows()
resized_thresh = cv2.resize(th1, down_points, interpolation= cv2.INTER_LINEAR)
cv2.imshow('Resized Down by defining height and width', resized_thresh) #display the resized thresholded image
cv2.waitKey(0)
cv2.destroyAllWindows()
