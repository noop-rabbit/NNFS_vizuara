import numpy as np
#print(np.__version__)

inputs = np.array([1, 2, 3, 4])

weights = np.array([
    [0.1, 0.2, 0.3, 0.4],
    [0.5, 0.6, 0.7, 0.8],
    [0.9, 1.0, 1.1, 1.2],
])

biases = np.array([0.1, 0.2, 0.3])

lr = 0.001        #learning rate

def relu(x):
    return np.where(x > 0, x, 0)

def relu_grad(x):
    return np.where(x > 0, 1, 0)

for iteration in range(100):
    z = np.dot(weights, inputs) + biases
    a = relu(z)
    y = np.sum(a)

    loss = y ** 2

    dL_dy = 2 * y
    dy_da = np.ones_like(a)
   
    dL_da = dL_dy * dy_da
    da_dz = relu_grad(z)

    dL_dz = dL_da * da_dz
    
    dL_dW = np.outer(dL_dz, inputs)
    dL_db = dL_dz

    weights -= lr * dL_dW
    biases -= lr * dL_db

    if iteration % 1 == 0:
        print(f"iteration: {iteration}, Loss: {loss}")

print(f"Final weights:\n {weights}")
print(f"Final biases:\n {biases}")