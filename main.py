from tensorflow import keras
from tensorflow.keras import layers

# Create a networkth 1 linear unit
model = keras.Sequential([
    layers.Dense(unit =1, input_shape=[3])
])

