from tensorflow import keras
from tensorflow._api.v2.keras import layers

# Create a networkth 1 linear unit
model = keras.Sequential([
    layers.Dense(unit =1, input_shape=[3])
])

