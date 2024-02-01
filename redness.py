class redness:

    def __init__(self, image):
        self.image = self.canny_method(self.gaussian_filter(self.redness_method(self.skin_segmentation(self.resize_image(image)))))
    
    def resize_image(self, image):
        # Resize Image: resize when its number of rows or columns exceeds 500 pixels
            # if number of rows exceeds 500 and is longer than columns
                # reduced to 480 pixels
                # adjust columns accordingly
            # if number of columns exceeds 500 and is longer than rows
                # reduced to 480 pixels
                # adjust rows accordingly
        pass

    def skin_segmentation(self, image):
        # Skin Segmentation: separating the skin from the background
            # using K-Means in HSV color space
            # converted to HSV color space (HSV Image)
            # segmented according to a threshold value (Segmented HSV Image)
                # threshold values are less than and equal to 25 for the Hue layer 
                # between 0.15 to 0.9 for the Saturation layer
            # cluserted using K-Means clustering
                # number of K for K-means clustering is 3 (K = total number of cluster; randomly determined)
                    # skin, non-skin, and background    
                # assign a data to a particular cluster according to the distance between the data and the centroid of the K cluster
                    # assigned to cluster with nearest centroid
            # highest number of members (Skin Image) = skin objects taken
                # assuming that the skin is the most dominant color in the image
        pass

    def redness_method(self, image):
        # Redness Method: calculating the redness value of each pixel
            # First obtain the RGB value of each pixel
            # Redness value of each pixel = max{0, (2R-(G+B)/R)}^2
                # R, G, B are the RGB values of the pixel
            # Threshold = Median of those redness values of all pixels
            # Omit the pixels with redness values less than the threshold
            # Each pixel with redness value greater than the threshold is considered as a red pixel
                # Redness Candidate Image Obtained
        pass

    def gaussian_filter(self, image):
        # Gaussian Filter: smoothing and reducing noise
            # Apply Gaussian filter to the Redness Candidate Image
                # Standard deviation = 0.5
                # Gaussian Filtered Image Obtained
            # Gaussian Redness 1 Image
                # If pixel value = 76 in the Gaussian Filtered Image
                    # Pixel value in the Redness Image is retained
                # Otherwise change pixel value to 0 (Guassian Image 1)
            # Gaussian Redness 2 Image
                # If pixel value in Gaussian Redness 1 Image < 1: retain
                # Otherwise change pixel value to 0 (Gaussian Image 2)
            # Gaussian Redness 3 Image
                # If area > 90 in the Gaussian Redness 2 Image: retain
                # Otherwise eliminated (Area Image)
            # Non-Redness Objects eliminated by threshold from Redness Method in Original Image
                # lower threshold value = (Mean intensity value in the Red layer)-1.32*(Standard deviation of the intensity value in the Red layer)
                # upper threshold value = (Mean intensity value in the Red layer)+1.32*(Standard deviation of the intensity value in the Red layer)
                # Do the same for the Green and Blue layers
            # If redness object candidate in Area Image has an avg intensity of RGB color in those range thresholds: retain
            # Otherwise eliminated (RGB Eliminated Image)
            # Non-redness objects eliminated by threshold according to Hue color value in Original Image
                # lower threshold = (Mean intensity value in Hue layer)-1.16*(Standard deviation of the intensity value in Hue layer)
                # upper threshold = (Mean intensity value in Hue layer)+0.5*(Standard deviation of the intensity value in Hue layer)
            # If redness object candidate in RGB Eliminated Image has an avg intensity of Hue color in those range thresholds: retain
            # Otherwise eliminated (Hue Eliminated Image)
        pass

    def canny_method(self, image):
        # Canny Method: Marks redness objects obtained from the Hue Eliminated Image
            # Detect edge pixels of each redness objects in Hue Eliminated Image
            # Change the intensity value of those edge pixels to red
        pass
