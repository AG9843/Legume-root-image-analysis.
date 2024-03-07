import cv2 #import cv2 library
img = cv2.imread('D:/root.tiff') #importation of the root image set your file location
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #conversion of root image into grayscale 
blur = cv2.medianBlur(gray,5) #use of median blur for edge smoothening 
ret, thresh = cv2.threshold(gray,170,255,cv2.THRESH_BINARY_INV) #thresholding of thegrayscale image using global threshold value of 170, 255blur = cv2.medianBlur(img,5) #use of median blur
ret3, thresh_Otsu = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU) # Otsu's thresholding after median blur
Mean_adap = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV,9,2) #use of mean adaptive threshold
Gaussian_adap = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,9,2)
ret3, Triangle = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_TRIANGLE)
down_width = 1000 #down size the width of the image
down_height = 1000 #down size the height of the image
down_points = (down_width, down_height)
resized_down = cv2.resize(thresh, down_points, interpolation= cv2.INTER_LINEAR)
cv2.imshow('Resized Down by defining height and width', resized_down) #display the resized image
cv2.waitKey(0) # we can observe the image until we press any key
num_components, labels, stats, centroids = cv2.connectedComponentsWithStats(thresh) #use connected component with stat function, for other threshold their respective names can be used 
areas = stats[:, cv2.CC_STAT_AREA]
areas = list(sorted(areas))
assert len(areas) >= 2
total_area = 0
noise_threshold = 250 #set the noise threshold for particle clearing 
for i, area in enumerate(areas[:-1]):
    print(f"Area of root part #{i} is: {area}") #displays areas of every connected pixels parts
    if area > noise_threshold:
        total_area += area
        areacm = total_area/24964 # conversion of number of pixels into standard value of cm2
print(f"Total projected area is: {areacm}") #print the projected area in cm2 
print(f"Total root surface area is: {areacm* 3.14159265}") #print the surface area in cm2
