#detect the brand names from the objects from the image
import easyocr
import matplotlib.pyplot as plt
import cv2

# Initialize the reader with the required language (e.g., English)
reader = easyocr.Reader(['en'])

fmcg_brands = [
    "Nestlé", "Procter & Gamble", "PepsiCo", "Unilever", "Coca-Cola",
    "L'Oréal", "Colgate-Palmolive", "Johnson & Johnson", "Kraft Heinz", "Mondelez International",
    "Reckitt Benckiser", "Danone", "Kimberly-Clark", "General Mills", "Mars, Incorporated",
    "Henkel", "Kellogg's", "Diageo", "Heineken", "AB InBev",
    "Pepsi", "Nivea", "Dove", "Gillette", "Pantene",
    "Oral-B", "Head & Shoulders", "Ariel", "Tide", "Whirlpool",
    "Maggi", "Nescafé", "KitKat", "Oreo", "Cadbury",
    "Lay's", "Doritos", "Mountain Dew", "Sprite", "Fanta",
    "Red Bull", "Lipton", "Hellmann's", "Knorr", "Ben & Jerry's",
    "Hershey's","Quaker","Pringles","Old Spice","Vaseline"
]
# Read the image
image_path = r'/content/WhatsApp Image 2024-10-20 at 01.01.43_497f5c0a.jpg' # Replace with the path to your image
image = cv2.imread(image_path)

# Use EasyOCR to detect text in the image
result = reader.readtext(image_path)

# Display the results
for (bbox, text, prob) in result:
    print(f"Text: {text}, Probability: {prob}")

# Optionally, display the image with bounding boxes around the detected text


for (bbox, text, prob) in result:
    # Unpack the bounding box
    (top_left, top_right, bottom_right, bottom_left) = bbox
    
    # Draw the bounding box
    cv2.rectangle(image, (int(top_left[0]), int(top_left[1])), 
                  (int(bottom_right[0]), int(bottom_right[1])), (0, 255, 0), 2)
    
    # Put the detected text near the box
    cv2.putText(image, text, (int(top_left[0]), int(top_left[1]) - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    
# Display the image with annotations
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()