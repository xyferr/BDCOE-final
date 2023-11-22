import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
from tensorflow.keras.optimizers import Adam 


# Function to preprocess the image
num_classes = 2
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize the image
    return img_array

def create_mobilenet_model():
    base_model = tf.keras.applications.MobileNetV2(input_shape=(224, 224, 3),
                                                   include_top=False,
                                                   weights='imagenet')
    base_model.trainable = False

    model = Sequential([
        base_model,
        GlobalAveragePooling2D(),
        Dense(256, activation='relu'),
        Dense(num_classes, activation='softmax')
    ])

    model.compile(optimizer=Adam(lr=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

    return model


mobilenet_model = create_mobilenet_model()

# Load the weights from the checkpoint file
mobilenet_model.load_weights('mobilenet_checkpoint_accuracy.h5')

# Preprocess an example image
example_image_path = r'Testing\Endangered\African Wild Dog\22.jpeg'
example_img_array = preprocess_image(example_image_path)

# Make a prediction
prediction = mobilenet_model.predict(example_img_array)

# Display the result
print("Prediction:", prediction)
