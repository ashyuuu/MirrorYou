import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load the trained model
model = load_model('model')

# Define image dimensions
image_height = 128
image_width = 128

def detect_redness(image_path):
    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(image_height, image_width))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0  # Normalize the image

    # Use the model to predict redness probability
    prediction = model.predict(img)
    print(prediction)
    
    # Threshold the prediction (example threshold is 0.5)
    redness_detected = prediction[0][0] > 0.45
    
    return redness_detected

# Example usage:
image_path = '/Users/li-yuho/Documents/GitHub/MirrorYou/photos/train/not_red/right_side5.jpg'
is_redness_detected = detect_redness(image_path)
print("Redness Detected:", is_redness_detected)
