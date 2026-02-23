"""
dot_product.py

Core dot product operations for AI / Machine Learning.
Vectors are assumed to be 1D NumPy arrays in R^n.
"""

from typing import Tuple
import numpy as np

Vector = np.ndarray


# ---------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------

def _validate_same_dimension(a: Vector, b: Vector) -> None:
    if a.ndim != 1 or b.ndim != 1:
        raise ValueError("Inputs must be 1D vectors.")

    if a.shape[0] != b.shape[0]:
        raise ValueError(
            f"Dimension mismatch: {a.shape} vs {b.shape}"
        )


# ---------------------------------------------------------------------
# Algebraic Dot Product
# ---------------------------------------------------------------------

def dot(a: Vector, b: Vector) -> float:
    """
    Compute dot product:

        a · b = Σ (a_i * b_i)

    Returns scalar.
    """
    _validate_same_dimension(a, b)
    return float(np.dot(a, b))


# ---------------------------------------------------------------------
# Manual Implementation (Educational Only)
# ---------------------------------------------------------------------

def manual_dot(a: Vector, b: Vector) -> float:
    """
    Pure Python dot product.
    O(n). Educational only.
    """
    _validate_same_dimension(a, b)
    return sum(a[i] * b[i] for i in range(len(a)))


# ---------------------------------------------------------------------
# Geometric Interpretation
# ---------------------------------------------------------------------

def norm(a: Vector) -> float:
    """L2 norm: ||a||"""
    return float(np.linalg.norm(a))


def cosine_similarity(a: Vector, b: Vector) -> float:
    """
    cos(θ) = (a · b) / (||a|| ||b||)
    """
    _validate_same_dimension(a, b)

    norm_a = norm(a)
    norm_b = norm(b)

    if norm_a == 0 or norm_b == 0:
        raise ValueError("Cannot compute cosine similarity with zero vector.")

    return dot(a, b) / (norm_a * norm_b)


# ---------------------------------------------------------------------
# Projection
# ---------------------------------------------------------------------

def projection(a: Vector, b: Vector) -> Vector:
    """
    Projection of a onto b:

        proj_b(a) = (a · b / b · b) b
    """
    _validate_same_dimension(a, b)

    denom = dot(b, b)
    if denom == 0:
        raise ValueError("Cannot project onto zero vector.")

    scalar = dot(a, b) / denom
    return scalar * b


# ---------------------------------------------------------------------
# Neuron Computation
# ---------------------------------------------------------------------

def neuron_output(weights: Vector, inputs: Vector, bias: float) -> float:
    """
    Single neuron computation:

        z = w · x + b
    """
    return dot(weights, inputs) + bias


# ---------------------------------------------------------------------
# Example Usage
# ---------------------------------------------------------------------

if __name__ == "__main__":
    a = np.array([1.0, 2.0, 3.0])
    b = np.array([4.0, 5.0, 6.0])

    print("Dot: - 04_dot_product.py:122", dot(a, b))
    print("Manual Dot: - 04_dot_product.py:123", manual_dot(a, b))
    print("Cosine Similarity: - 04_dot_product.py:124", cosine_similarity(a, b))
    print("Projection of a onto b: - 04_dot_product.py:125", projection(a, b))

    x = np.array([0.5, 1.5, -0.5])
    w = np.array([0.2, -0.4, 0.6])
    b = 0.1
    print("Neuron Output: - 04_dot_product.py:130", neuron_output(w, x, b))