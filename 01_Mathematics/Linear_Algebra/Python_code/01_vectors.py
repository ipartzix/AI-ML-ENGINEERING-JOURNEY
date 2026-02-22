"""
vector_utils.py

Authoritative vector operations for Machine Learning.
All vectors are assumed to be 1D NumPy arrays in R^n.
"""

from typing import Union
import numpy as np

Vector = np.ndarray


# ---------------------------------------------------------------------
# Basic Validation
# ---------------------------------------------------------------------

def _validate_same_dimension(a: Vector, b: Vector) -> None:
    if a.shape != b.shape:
        raise ValueError("Vectors must have the same dimensions.")


# ---------------------------------------------------------------------
# Norms
# ---------------------------------------------------------------------

def l2_norm(x: Vector) -> float:
    """
    Compute Euclidean (L2) norm:
        ||x||_2 = sqrt(sum(x_i^2))
    """
    return np.linalg.norm(x, ord=2)


def l1_norm(x: Vector) -> float:
    """
    Compute L1 norm:
        ||x||_1 = sum(|x_i|)
    """
    return np.linalg.norm(x, ord=1)


def lp_norm(x: Vector, p: Union[int, float]) -> float:
    """
    General Lp norm:
        ||x||_p = (sum |x_i|^p)^(1/p)
    """
    if p <= 0:
        raise ValueError("p must be > 0.")
    return np.linalg.norm(x, ord=p)


# ---------------------------------------------------------------------
# Distance
# ---------------------------------------------------------------------

def euclidean_distance(a: Vector, b: Vector) -> float:
    """
    Euclidean distance:
        d(a, b) = ||a - b||_2
    """
    _validate_same_dimension(a, b)
    return l2_norm(a - b)


# ---------------------------------------------------------------------
# Dot Product
# ---------------------------------------------------------------------

def dot_product(a: Vector, b: Vector) -> float:
    """
    Algebraic definition:
        a · b = sum(a_i * b_i)
    """
    _validate_same_dimension(a, b)
    return float(np.dot(a, b))


# ---------------------------------------------------------------------
# Cosine Similarity
# ---------------------------------------------------------------------

def cosine_similarity(a: Vector, b: Vector) -> float:
    """
    cos(theta) = (a · b) / (||a|| ||b||)
    """
    _validate_same_dimension(a, b)

    norm_a = l2_norm(a)
    norm_b = l2_norm(b)

    if norm_a == 0 or norm_b == 0:
        raise ValueError("Cannot compute cosine similarity with zero vector.")

    return dot_product(a, b) / (norm_a * norm_b)


# ---------------------------------------------------------------------
# Projection
# ---------------------------------------------------------------------

def projection(a: Vector, b: Vector) -> Vector:
    """
    Projection of vector a onto vector b:

        proj_b(a) = (a · b / b · b) * b
    """
    _validate_same_dimension(a, b)

    denom = dot_product(b, b)
    if denom == 0:
        raise ValueError("Cannot project onto zero vector.")

    scalar = dot_product(a, b) / denom
    return scalar * b


# ---------------------------------------------------------------------
# Orthogonality
# ---------------------------------------------------------------------

def is_orthogonal(a: Vector, b: Vector, tol: float = 1e-10) -> bool:
    """
    Check orthogonality:
        a · b ≈ 0
    """
    _validate_same_dimension(a, b)
    return abs(dot_product(a, b)) < tol


# ---------------------------------------------------------------------
# Example Usage
# ---------------------------------------------------------------------

if __name__ == "__main__":
    x = np.array([2.0, -1.0, 4.0])
    y = np.array([1.0, 3.0, -2.0])

    print("L2 Norm: - 01_vectors.py:139", l2_norm(x))
    print("L1 Norm: - 01_vectors.py:140", l1_norm(x))
    print("Distance: - 01_vectors.py:141", euclidean_distance(x, y))
    print("Dot Product: - 01_vectors.py:142", dot_product(x, y))
    print("Cosine Similarity: - 01_vectors.py:143", cosine_similarity(x, y))
    print("Projection of x onto y: - 01_vectors.py:144", projection(x, y))
    print("Orthogonal?: - 01_vectors.py:145", is_orthogonal(x, y))