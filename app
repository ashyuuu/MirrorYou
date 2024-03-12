import numpy as np
from keras.models import load_model
from keras.preprocessing import image

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
image_path = '/Users/Ashley/Documents/GitHub/MirrorYou/twice.png'
is_redness_detected = detect_redness(image_path)
print("Redness Detected:", is_redness_detected)

image_path = '/Users/Ashley/Documents/GitHub/MirrorYou/photos/test/red/acne-18-_png.rf.a478012afc375620f9f760c4a3a302d3.jpg'
is_redness_detected = detect_redness(image_path)
print("Redness Detected:", is_redness_detected)

image_path = '/Users/Ashley/Documents/GitHub/MirrorYou/photos/test/not_red/11.jpg'
is_redness_detected = detect_redness(image_path)
print("Redness Detected:", is_redness_detected)

