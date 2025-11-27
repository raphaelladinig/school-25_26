import numpy as np
from keras.datasets import reuters
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, Dropout

num_words = 10000
maxlen = 200

print("Lade Daten...")
(x_train, y_train), (x_test, y_test) = reuters.load_data(num_words=num_words)

x_train = pad_sequences(x_train, maxlen=maxlen)
x_test = pad_sequences(x_test, maxlen=maxlen)

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
num_classes = y_train.shape[1]

print(f"x_train shape: {x_train.shape}")
print(f"y_train shape: {y_train.shape}")

model = Sequential()
model.add(Embedding(input_dim=num_words, output_dim=128, input_length=maxlen))
model.add(LSTM(64, return_sequences=False)) 
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax')) 

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

history = model.fit(x_train, y_train,
                    epochs=10,
                    batch_size=32,
                    validation_split=0.2)

results = model.evaluate(x_test, y_test)
print(f"Test Loss: {results[0]}, Test Accuracy: {results[1]}")

label_names = [
    "cocoa", "grain", "veg-oil", "earn", "acq", "wheat", "corn", "crude",
    "money-fx", "interest", "ship", "trade", "reserves", "cotton", "coffee",
    "sugar", "gold", "tin", "strategic-metal", "livestock", "retail", "ipi",
    "iron-steel", "rubber", "heat", "jobs", "lei", "bop", "carcass",
    "money-supply", "alum", "oilseed", "meal-feed", "cpi", "housing",
    "rubber", "zinc", "nickel", "orange", "pet-chem", "dlr", "gas", "silver",
    "wpi", "strategic-reserves", "wheat-germ"
]

prediction = model.predict(x_test[:1])
predicted_class = np.argmax(prediction)
true_class = np.argmax(y_test[0])

print(f"\nBeispiel Vorhersage:")
print(f"Wahre Klasse: {true_class} ({label_names[true_class]})")
print(f"Vorhergesagt: {predicted_class} ({label_names[predicted_class]})")
