from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os


def predict_disease(image_path):
    h5_file_path = os.path.join(os.path.dirname(__file__), 'models', 'finetune_model.h5')  # Adjust the path as needed
    model = load_model(h5_file_path)

    # image using Keras' image.load_img function
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    processed_img = img_array / 255.0  # Normalize pixel values
    print("done")

    # Perform predictions using the loaded model
    prediction = model.predict(processed_img)

    class_indices = {0: 'CNV', 1: 'DME', 2: 'DRUSEN', 3: 'NORMAL'}
    # Get probabilities for each class
    probabilities = {class_indices[i]: prob for i, prob in enumerate(prediction[0])}

    return probabilities


# from keras.models import load_model
# from keras.optimizers import Adam
# from keras.preprocessing import image
# import numpy as np
# import os

# # Define the custom optimizer if needed
# custom_objects = {'Adam': Adam}

# def predict_disease(image_path):
#     # Load your .h5 model file
#     h5_file_path = os.path.join(os.path.dirname(__file__), 'models', 'finetune_model.h5')  # Adjust the path as needed
#     model = load_model(h5_file_path, custom_objects=custom_objects)

#     # Load the image using Keras' image.load_img function
#     img = image.load_img(image_path, target_size=(224, 224))
#     img_array = image.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0)

#     # Preprocess the image according to your model's requirements
#     processed_img = img_array / 255.0  # Normalize pixel values

#     # Perform predictions using the loaded model
#     prediction = model.predict(processed_img)

#     class_indices = {0: 'CNV', 1: 'DME', 2: 'DRUSEN', 3: 'NORMAL'}
#     # Assuming your model outputs class probabilities
#     predicted_class = class_indices[np.argmax(prediction)]
#     confidence = np.max(prediction) * 100  # Assuming confidence is max probability

#     return {'class': predicted_class, 'confidence': confidence}
