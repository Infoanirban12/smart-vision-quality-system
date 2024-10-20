import easyocr
from skimage import io, restoration
import cv2
import numpy as np
import matplotlib.pyplot as plt

reader = easyocr.Reader(['en'])

image_path = '/content/img_sauce.jpg'    # Path to the image

def preprocess_image(image_path):

    image = io.imread(image_path)
    if image.shape[2] == 4:
        image = image[..., :3] # Removing the alpha channel

    denoised_image = restoration.denoise_bilateral(image, channel_axis=-1) # Convert to grayscale

    denoised_image = (denoised_image * 255).astype(np.uint8)

    return denoised_image

img = preprocess_image(image_path)

result = reader.readtext(img)

for (bbox, text, prob) in result:
    print(f"Detected text: {text} (Confidence: {prob:.2f})")

for (bbox, text, prob) in result:
    # Extracting the bounding box coordinates
    (top_left, top_right, bottom_right, bottom_left) = bbox

    # Drawing the bounding box around the text
    cv2.rectangle(img, (int(top_left[0]), int(top_left[1])),
                  (int(bottom_right[0]), int(bottom_right[1])), (0, 255, 0), 2)

    # Putting the detected text near the box
    cv2.putText(img, text, (int(top_left[0]), int(top_left[1]) - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
# Displaying the image
plt.imshow(img)
plt.axis('on')
plt.show()
