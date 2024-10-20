import cv2 as cv
from google.colab.patches import cv2_imshow

# Load the image
image_path = '/content/407f3487-IMG-20241012-WA0010.jpg'
image = cv.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print(f"Error: Could not load image from {image_path}. Please check the path.")
    exit()

# Convert the image to grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Apply a Gaussian blur to reduce noise and improve contour detection
gray_blurred = cv.GaussianBlur(gray, (5, 5), 0)

# Apply a binary threshold to the image (adjust threshold as needed)
_, binary = cv.threshold(gray_blurred, 120, 255, cv.THRESH_BINARY_INV)

# Optionally, use Canny edge detection for better contour detection
# binary = cv.Canny(gray_blurred, 100, 200)

# Find contours in the binary image
contours, _ = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Optionally, filter out small contours (e.g., noise) based on contour area
min_area = 100  # Adjust this value based on the image and expected object size
filtered_contours = [cnt for cnt in contours if cv.contourArea(cnt) > min_area]

# Count the number of contours after filtering
num_objects = len(filtered_contours)

print(f'Number of objects detected: {num_objects}')

# Optionally, draw the contours on the original image
cv.drawContours(image, filtered_contours, -1, (0, 255, 0), 2)

# Show the resulting image with contours
cv2_imshow(image)
cv.waitKey(0)
cv.destroyAllWindows()