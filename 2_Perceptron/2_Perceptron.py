import numpy as np

# Función de activación step function
def step_function(x):
    return 1 if x >= 0 else 0

# Inicializar pesos y sesgo
weights = np.array([0.5, 0.5])
bias = -0.5

# Datos de entrada y salida
input_data = np.array([1, 1])  # ejemplo de datos
expected_output = 1  # clase esperada

# Calculo de la salida del perceptrón
weighted_sum = np.dot(input_data, weights) + bias
output = step_function(weighted_sum)

print("Output:", output)
print("Expected Output:", expected_output)
