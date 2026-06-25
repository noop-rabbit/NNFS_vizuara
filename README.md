# Neural Networks From Scratch (NNFS)

A hands-on implementation of Neural Networks from Scratch using NumPy. This repository follows a progressive learning path that starts with the fundamentals of vectorized computation and gradually builds toward a complete neural network capable of classifying handwritten digits from the MNIST dataset.

## Repository Goal

The primary objective of this project is to understand the internal mechanics of neural networks without relying on high-level deep learning frameworks such as TensorFlow or PyTorch.

By implementing every component manually, including forward propagation, loss computation, backpropagation, and optimization algorithms, you gain a deeper understanding of how neural networks learn.

---

## Learning Roadmap

### Phase 1 — Foundations

**Notebooks**

* `NNFS1.ipynb`
* `NNFS2_numpy.ipynb`
* `NNFS4_broadcast.ipynb`

**Topics Covered**

* NumPy fundamentals
* Array creation and manipulation
* Matrix operations
* Shape transformations
* Broadcasting rules
* Vectorized computation

**Learning Outcome**

Understand how neural network computations can be efficiently expressed using matrix operations.

---

### Phase 2 — Core Components

**Notebooks**

* `NNFS3_Dense_layer.ipynb`
* `NNFS5_Activation_Fn.ipynb`

**Topics Covered**

* Dense (Fully Connected) Layers
* Weight initialization
* Bias handling
* Activation Functions

  * ReLU
  * Softmax
  * Other common activations

**Learning Outcome**

Build the fundamental building blocks used in neural networks.

---

### Phase 3 — Forward Propagation

**Notebook**

* `NNFS6_Forward_Pass.ipynb`

**Topics Covered**

* Layer chaining
* Forward pass execution
* Data flow through a network

**Learning Outcome**

Understand how inputs are transformed into predictions through successive layers.

---

### Phase 4 — Loss Functions

**Notebooks**

* `NNFS7_Loss.ipynb`
* `NNFS11_crossEntropy_grad.ipynb`

**Topics Covered**

* Measuring prediction error
* Categorical Cross-Entropy Loss
* Confidence scores
* Loss gradients

**Learning Outcome**

Learn how a neural network evaluates the quality of its predictions.

---

### Phase 5 — Backpropagation

**Files**

* `NNFS8_Backprop.ipynb`
* `NNFS9_Backprop_batch.py`
* `NNFS10_Backprop_batch1.ipynb`
* `NNFS12_BP+CE+SM.ipynb`

**Topics Covered**

* Chain Rule
* Gradient computation
* Batch processing
* Weight and bias gradients
* Softmax + Cross-Entropy optimization

**Learning Outcome**

Understand the mathematical engine that enables neural networks to learn from data.

---

### Phase 6 — Optimization

**Notebooks**

* `Adagrad_RMSProp.ipynb`
* `NNFS13_FP+BP+GD+ADAM.ipynb`

**Topics Covered**

* Gradient Descent
* Learning Rate Management
* AdaGrad
* RMSProp
* Adam Optimizer

**Learning Outcome**

Explore techniques that improve convergence speed and training stability.

---

### Phase 7 — Final Application

**Notebook**

* `Hands_on_MNIST.ipynb`

**Topics Covered**

* MNIST Dataset
* End-to-End Training Pipeline
* Model Evaluation
* Prediction Analysis

**Learning Outcome**

Combine all previously implemented components into a complete neural network capable of handwritten digit classification.

---

## Recommended Study Order

| Order | File                           |
| ----- | ------------------------------ |
| 1     | NNFS1.ipynb                    |
| 2     | NNFS2_numpy.ipynb              |
| 3     | NNFS4_broadcast.ipynb          |
| 4     | NNFS3_Dense_layer.ipynb        |
| 5     | NNFS5_Activation_Fn.ipynb      |
| 6     | NNFS6_Forward_Pass.ipynb       |
| 7     | NNFS7_Loss.ipynb               |
| 8     | NNFS8_Backprop.ipynb           |
| 9     | NNFS9_Backprop_batch.py        |
| 10    | NNFS10_Backprop_batch1.ipynb   |
| 11    | NNFS11_crossEntropy_grad.ipynb |
| 12    | NNFS12_BP+CE+SM.ipynb          |
| 13    | Adagrad_RMSProp.ipynb          |
| 14    | NNFS13_FP+BP+GD+ADAM.ipynb     |
| 15    | Hands_on_MNIST.ipynb           |

---

## Tips for Learners

### Focus on Understanding the "Why"

If you encounter difficulties during backpropagation, revisit:

* `NNFS6_Forward_Pass.ipynb`
* `NNFS7_Loss.ipynb`

These notebooks establish the intuition required for understanding gradient flow and parameter updates.

### Track Hyperparameters

When experimenting with optimizers, document:

* Learning Rate
* Decay
* Epsilon
* Batch Size
* Epoch Count

Keeping notes on hyperparameter choices makes future experimentation easier.

### Experiment Frequently

Try modifying:

* Number of neurons
* Number of layers
* Activation functions
* Optimizers

Observe how these changes affect convergence and model performance.

---

## Technologies Used

* Python
* NumPy
* Matplotlib
* Jupyter Notebook

---

## References

* Neural Networks from Scratch
* NumPy Documentation
* Deep Learning Fundamentals
* MNIST Dataset

---

## Final Goal

By the end of this repository, you will have implemented:

* Dense Layers
* Activation Functions
* Forward Propagation
* Cross-Entropy Loss
* Backpropagation
* Gradient Descent
* AdaGrad
* RMSProp
* Adam Optimizer

and trained a complete neural network from scratch without using a deep learning framework.
