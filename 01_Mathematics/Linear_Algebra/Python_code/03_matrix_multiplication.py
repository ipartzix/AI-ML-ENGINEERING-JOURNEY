"""
matrix_multiplication.py

Authoritative implementation of matrix multiplication
for AI / Machine Learning workflows.
"""

from typing import Tuple
import numpy as np

Matrix = np.ndarray


# ---------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------

def _validate_multiplication_shapes(A: Matrix, B: Matrix) -> None:
    """
    Ensure A (m×n) and B (n×p) are compatible.
    """
    if A.ndim != 2 or B.ndim != 2:
        raise ValueError("Both inputs must be 2D matrices.")

    if A.shape[1] != B.shape[0]:
        raise ValueError(
            f"Incompatible shapes: {A.shape} cannot be multiplied with {B.shape}"
        )


# ---------------------------------------------------------------------
# Core Implementation
# ---------------------------------------------------------------------

def matmul(A: Matrix, B: Matrix) -> Matrix:
    """
    Matrix multiplication:

        If A ∈ R^(m×n)
        and B ∈ R^(n×p)
        then C = AB ∈ R^(m×p)

    Uses optimized NumPy backend (BLAS).
    """
    _validate_multiplication_shapes(A, B)
    return A @ B


# ---------------------------------------------------------------------
# Manual Implementation (Educational Only)
# ---------------------------------------------------------------------

def manual_matmul(A: Matrix, B: Matrix) -> Matrix:
    """
    Pure Python implementation for learning purposes.
    Not optimized. O(mnp).
    """
    _validate_multiplication_shapes(A, B)

    m, n = A.shape
    _, p = B.shape

    result = np.zeros((m, p))

    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i, j] += A[i, k] * B[k, j]

    return result


# ---------------------------------------------------------------------
# Identity Matrix
# ---------------------------------------------------------------------

def identity(n: int) -> Matrix:
    """
    Identity matrix I_n ∈ R^(n×n)
    """
    return np.eye(n)


# ---------------------------------------------------------------------
# Properties Demonstration
# ---------------------------------------------------------------------

def associative_property(A: Matrix, B: Matrix, C: Matrix) -> bool:
    """
    Check (AB)C == A(BC)
    """
    _validate_multiplication_shapes(A, B)
    _validate_multiplication_shapes(B, C)

    left = matmul(matmul(A, B), C)
    right = matmul(A, matmul(B, C))

    return np.allclose(left, right)


def distributive_property(A: Matrix, B: Matrix, C: Matrix) -> bool:
    """
    Check A(B + C) == AB + AC
    """
    _validate_multiplication_shapes(A, B)
    _validate_multiplication_shapes(A, C)

    left = matmul(A, B + C)
    right = matmul(A, B) + matmul(A, C)

    return np.allclose(left, right)


# ---------------------------------------------------------------------
# Example Usage
# ---------------------------------------------------------------------

if __name__ == "__main__":
    A = np.array([[1, 2], [3, 4]], dtype=float)
    B = np.array([[5, 6], [7, 8]], dtype=float)

    print("Matrix Product:\n - 03_matrix_multiplication.py:122", matmul(A, B))
    print("Manual Product:\n - 03_matrix_multiplication.py:123", manual_matmul(A, B))

    I = identity(2)
    print("Identity Check:\n - 03_matrix_multiplication.py:126", matmul(I, A))