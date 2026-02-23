"""
norms_distance.py

Vector norm and distance utilities for AI / Machine Learning.
All vectors assumed to be 1D NumPy arrays in R^n.
"""

from typing import Union
import numpy as np

Vector = np.ndarray


# ---------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------

def _validate_vector(x: Vector) -> None:
    if x.ndim != 1:
        raise ValueError("Input must be a 1D vector.")


def _validate_same_dimension(x: Vector, y: Vector) -> None:
    _validate_vector(x)
    _validate_vector(y)

    if x.shape[0] != y.shape[0]:
        raise ValueError(
            f"Dimension mismatch: {x.shape} vs {y.shape}"
        )


# ---------------------------------------------------------------------
# Norms
# ---------------------------------------------------------------------

def l2_norm(x: Vector) -> float:
    """
    Euclidean norm:
        ||x||_2 = sqrt(sum(x_i^2))
    """
    _validate_vector(x)
    return float(np.linalg.norm(x, ord=2))


def l1_norm(x: Vector) -> float:
    """
    Manhattan norm:
        ||x||_1 = sum |x_i|
    """
    _validate_vector(x)
    return float(np.linalg.norm(x, ord=1))


def linf_norm(x: Vector) -> float:
    """
    Infinity norm:
        ||x||_∞ = max |x_i|
    """
    _validate_vector(x)
    return float(np.linalg.norm(x, ord=np.inf))


def lp_norm(x: Vector, p: Union[int, float]) -> float:
    """
    General p-norm:
        ||x||_p = (sum |x_i|^p)^(1/p)
    """
    _validate_vector(x)

    if p <= 0:
        raise ValueError("p must be > 0.")

    return float(np.linalg.norm(x, ord=p))


# ---------------------------------------------------------------------
# Distance Metrics
# ---------------------------------------------------------------------

def euclidean_distance(x: Vector, y: Vector) -> float:
    """
    L2 distance:
        d(x, y) = ||x - y||_2
    """
    _validate_same_dimension(x, y)
    return l2_norm(x - y)


def manhattan_distance(x: Vector, y: Vector) -> float:
    """
    L1 distance:
        d(x, y) = ||x - y||_1
    """
    _validate_same_dimension(x, y)
    return l1_norm(x - y)


def chebyshev_distance(x: Vector, y: Vector) -> float:
    """
    L∞ distance:
        d(x, y) = ||x - y||_∞
    """
    _validate_same_dimension(x, y)
    return linf_norm(x - y)


# ---------------------------------------------------------------------
# Example Usage
# ---------------------------------------------------------------------

if __name__ == "__main__":
    x = np.array([3.0, 4.0])
    y = np.array([1.0, 2.0])

    print("L2 Norm: - 05_norms_distance.py:116", l2_norm(x))
    print("L1 Norm: - 05_norms_distance.py:117", l1_norm(x))
    print("L∞ Norm: - 05_norms_distance.py:118", linf_norm(x))
    print("p=3 Norm: - 05_norms_distance.py:119", lp_norm(x, 3))

    print("Euclidean Distance: - 05_norms_distance.py:121", euclidean_distance(x, y))
    print("Manhattan Distance: - 05_norms_distance.py:122", manhattan_distance(x, y))
    print("Chebyshev Distance: - 05_norms_distance.py:123", chebyshev_distance(x, y))