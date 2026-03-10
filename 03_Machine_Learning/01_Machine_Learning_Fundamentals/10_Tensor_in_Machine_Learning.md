# Tensor in Machine Learning

## 1. Introduction

A **Tensor** is a fundamental data structure used in machine learning and deep learning.  
It is a **generalized form of arrays and matrices that can represent data in multiple dimensions**.

In simple terms:

- Scalar → single number  
- Vector → 1D array  
- Matrix → 2D array  
- Tensor → multi-dimensional array (3D, 4D, or higher)

Tensors allow machine learning frameworks to efficiently handle **large-scale numerical data and perform complex mathematical operations**.

---

# 2. Types of Tensors by Dimension

Tensors are classified based on their **number of dimensions**, also called **rank**.

| Tensor Type | Dimension | Example |
|------|------|------|
| Scalar | 0D | Temperature value |
| Vector | 1D | List of numbers |
| Matrix | 2D | Table of numbers |
| 3D Tensor | 3D | Color image |
| Higher-Dimensional Tensor | 4D+ | Video or batches of images |

---

# 3. Scalar (0D Tensor)

A **scalar** is a single numeric value.

Example:

```
5
```

Characteristics:

- No dimensions
- Represents a single value

Example in machine learning:

- Learning rate
- Loss value

---

# 4. Vector (1D Tensor)

A **vector** is a one-dimensional array of numbers.

Example:

```
[2, 4, 6, 8]
```

Characteristics:

- One dimension
- Represents a list of values

Example in ML:

- Feature vector of a data sample

Example:

```
[age, salary, experience]
```

---

# 5. Matrix (2D Tensor)

A **matrix** is a two-dimensional array organized into **rows and columns**.

Example:

```
[
 [1, 2, 3],
 [4, 5, 6]
]
```

Characteristics:

- Two dimensions
- Rows × Columns

Example in ML:

- Dataset representation
- Weight matrices in neural networks

---

# 6. 3D Tensor

A **3D tensor** represents data with three dimensions.

Example:

```
[
 [
  [1,2],
  [3,4]
 ],
 [
  [5,6],
  [7,8]
 ]
]
```

Example in ML:

A **color image**.

Images contain:

- Height
- Width
- Color channels (RGB)

Example:

```
Height × Width × Channels
```

Example:

```
224 × 224 × 3
```

---
# 7. Higher-Dimensional Tensors

Deep learning models often use **4D or higher-dimensional tensors**.

Example:

### Batch of Images

```
Batch Size × Height × Width × Channels
```

Example:

```
32 × 224 × 224 × 3
```

This means:

- 32 images
- each image 224×224 pixels
- 3 color channels

---

# 8. Why Tensors Are Important in Machine Learning

Tensors enable efficient processing of large datasets and complex operations.

### Key Advantages

#### 1. Efficient Computation

Tensors allow frameworks to perform **parallel mathematical operations** using GPUs and TPUs.

#### 2. Structured Data Representation

They represent complex data structures such as:

- Images
- Videos
- Text embeddings
- Neural network weights

#### 3. Compatibility with Deep Learning

All deep learning models operate on tensors.

---

# 9. Tensors in Neural Networks

Neural networks use tensors to store:

- Input data
- Weights
- Bias values
- Intermediate activations
- Output predictions

Example flow:

```
Input Tensor → Neural Network Layers → Output Tensor
```

Each layer performs **tensor operations such as matrix multiplication and transformations**.

---

# 10. Tensor Example in Python

Example using NumPy:

```python
import numpy as np

# Scalar
scalar = np.array(5)

# Vector
vector = np.array([1,2,3])

# Matrix
matrix = np.array([[1,2],[3,4]])

# 3D Tensor
tensor3d = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])

print(tensor3d.shape)
```

---
