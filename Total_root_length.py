import cv2 #import cv2 module
image = cv2.imread("D:/root.tiff") #provide the path of the image
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convert the image into grayscale form 
image = cv2.bitwise_not(image) #inverts the pixel value of the image
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
print(f"Total root length is: {TRL} cm") #print length in cm
down_points = (1000, 1000)
resized_thinned = cv2.resize(thinning, down_points, interpolation= cv2.INTER_LINEAR)
cv2.imshow('Resized Down by defining height and width', resized_thinned) #display the resized thinned image
cv2.waitKey(0)
cv2.destroyAllWindows()
