import tensorflow as tf

# Load model
model_path = "models/mnist_model.h5"
model = tf.keras.models.load_model(model_path)

# Perform validation
assert len(model.trainable_variables) < 25000, "Model exceeds 25,000 parameters."
assert model.input_shape == (None, 28, 28, 1), "Model input shape mismatch."
assert model.output_shape == (None, 10), "Model output shape mismatch."

# Test model accuracy
from tensorflow.keras.datasets import mnist
(_, _), (x_test, y_test) = mnist.load_data()
x_test = x_test.reshape(-1, 28, 28, 1).astype("float32") / 255.0
y_test = tf.keras.utils.to_categorical(y_test, 10)
loss, accuracy = model.evaluate(x_test, y_test)

assert accuracy > 0.95, f"Model accuracy is too low: {accuracy * 100:.2f}%"

print("All validation checks passed!")
