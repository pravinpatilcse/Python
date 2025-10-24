import cv2 as cv
import sys

# Read image in grayscale mode
img_path = r"C:\Users\Admin\Desktop\python_rpa\OpenCV_Photo\Pravin.png"
img = cv.imread(img_path, 0)

# Check if image was successfully loaded
if img is None:
    print(f"Error: Could not read image at {img_path}")
    sys.exit(1)

# Display the grayscale image
cv.imshow('Grayscale Image', img)

# Wait for any key press (0 means wait indefinitely)
cv.waitKey(0)

# Clean up
cv.destroyAllWindows()