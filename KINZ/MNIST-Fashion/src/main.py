import os
import numpy as np
import keras
from keras import layers
from keras.datasets import fashion_mnist
from PIL import Image
import matplotlib.pyplot as plt

class_names = [
    "T-shirt/Top",
    "Hose",
    "Pullover",
    "Kleid",
    "Mantel",
    "Sandalen",
    "Hemd",
    "Sneaker",
    "Tasche",
    "Halbschuhe",
]

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

# 1.1.1
print(f"Dimensionen der Trainingsbilder (x_train): {x_train.shape}")
print(f"Dimensionen der Trainingslabels (y_train): {y_train.shape}")
print(f"Dimensionen der Testbilder (x_test): {x_test.shape}")
print(f"Dimensionen der Testlabels (y_test): {y_test.shape}")

# 1.1.2
unique, counts = np.unique(y_train, return_counts=True)
for label, count in zip(unique, counts):
    print(f"- {class_names[label]}: {count} Bilder")

# 1.1.3
tenth_image_pixels = x_train[9]
tenth_image_label_index = y_train[9]
tenth_image_label_name = class_names[tenth_image_label_index]

# 1.2.1
plt.figure(figsize=(12, 12))
for i in range(100):
    plt.subplot(10, 10, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x_train[i])
    plt.xlabel(class_names[y_train[i]])

output_dir_viz = "output_visualisierung"
os.makedirs(output_dir_viz, exist_ok=True)
plt.savefig(os.path.join(output_dir_viz, "erste_100_bilder.png"))
print(
    f"Visualisierung der ersten 100 Bilder wurde in '{output_dir_viz}/erste_100_bilder.png' gespeichert."
)


# 1.2.2
base_export_dir = "fashion_mnist_kategorien"
num_images_to_export = 1000

for label_index, label_name in enumerate(class_names):
    category_dir = os.path.join(base_export_dir, f"{label_index}_{label_name}")
    os.makedirs(category_dir, exist_ok=True)

for i in range(num_images_to_export):
    image_array = x_train[i]
    label_index = y_train[i]
    label_name = class_names[label_index]

    im = Image.fromarray(image_array)

    category_dir = os.path.join(base_export_dir, f"{label_index}_{label_name}")
    im.save(os.path.join(category_dir, f"image_{i}.jpeg"))

print(
    f"{num_images_to_export} Bilder wurden in das Verzeichnis '{base_export_dir}' exportiert."
)


x_train_norm = x_train.astype("float32") / 255
x_test_norm = x_test.astype("float32") / 255

x_train_flat = x_train_norm.reshape(-1, 28 * 28)
x_test_flat = x_test_norm.reshape(-1, 28 * 28)

num_classes = 10
y_train_cat = keras.utils.to_categorical(y_train, num_classes)
y_test_cat = keras.utils.to_categorical(y_test, num_classes)

print(f"\nForm der flachen Trainingsbilder: {x_train_flat.shape}")
print(f"Form der kategorialen Trainingslabels: {y_train_cat.shape}")

# 2.1
model = keras.Sequential(
    [
        keras.Input(shape=(784,)),
        layers.Dense(128, activation="relu"),
        layers.Dense(24, activation="relu"),
        layers.Dense(num_classes, activation="softmax"),
    ]
)

# 2.2
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])


history = model.fit(
    x_train_flat, y_train_cat, batch_size=256, epochs=10, validation_split=0.1
)


# 3.1
score = model.evaluate(x_test_flat, y_test_cat)
print(f"Test loss: {score[0]:.4f}")
print(
    f"Test accuracy: {score[1]:.4f} (d.h. {score[1]*100:.2f}% der Testbilder korrekt klassifiziert)"
)


# 3.2
predictions = model.predict(x_test_flat)

# 3.3
output_model_dir = "output_model"
os.makedirs(output_model_dir, exist_ok=True)
model_path = os.path.join(output_model_dir, "fashion_mnist_model.keras")
model.save(model_path)
loaded_model = keras.models.load_model(model_path)
