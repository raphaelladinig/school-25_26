import keras
from keras import layers
import numpy as np

num_classes = 3
input_shape = (180, 180, 3)

# Create training and validation datasets
train_dataset = keras.preprocessing.image_dataset_from_directory(
    "./rps",
    image_size=(180, 180),
    label_mode="categorical",
    batch_size=32,
    validation_split=0.2,
    subset="training",
    seed=1337,
)
validation_dataset = keras.preprocessing.image_dataset_from_directory(
    "./rps",
    image_size=(180, 180),
    label_mode="categorical",
    batch_size=32,
    validation_split=0.2,
    subset="validation",
    seed=1337,
)

print(f"Class names: {train_dataset.class_names}")

model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation="softmax"),
    ]
)

model.summary()

model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# Train the model for 10 epochs
history = model.fit(
    train_dataset,
    epochs=10,
    validation_data=validation_dataset,
)

# Save the trained model
model.save("./out/model.keras")


def predict_image(model_path, img_path):
    model = keras.models.load_model(model_path)
    img = keras.preprocessing.image.load_img(
        img_path, target_size=(180, 180)
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Create batch axis

    predictions = model.predict(img_array)
    score = predictions[0]

    print(
        f"This image is %.2f percent rock, %.2f percent paper, and %.2f percent scissors."
        % (100 * score[0], 100 * score[1], 100 * score[2])
    )


# Example of how to use the prediction function:
# predict_image("./out/model.keras", "/path/to/your/image.png")
