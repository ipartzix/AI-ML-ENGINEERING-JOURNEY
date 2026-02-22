"""
matrix_utils.py

Core matrix operations for Machine Learning.
All matrices are assumed to be NumPy arrays in R^(m×n).
"""

from typing import Tuple
import numpy as np

Matrix = np.ndarray


# ---------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------

def _validate_same_shape(A: Matrix, B: Matrix) -> None:
    if A.shape != B.shape:
        raise ValueError("Matrices must have the same shape.")


def _validate_square(A: Matrix) -> None:
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix must be square.")


# ---------------------------------------------------------------------
# Basic Operations
# ---------------------------------------------------------------------

def add(A: Matrix, B: Matrix) -> Matrix:
    """Matrix addition: A + B"""
    _validate_same_shape(A, B)
    return A + B


def subtract(A: Matrix, B: Matrix) -> Matrix:
    """Matrix subtraction: A - B"""
    _validate_same_shape(A, B)
    return A - B


def scalar_multiply(A: Matrix, scalar: float) -> Matrix:
    """Scalar multiplication: cA"""
    return scalar * A


def multiply(A: Matrix, B: Matrix) -> Matrix:
    """
    Matrix multiplication:
        (m×n) · (n×p) → (m×p)
    """
    if A.shape[1] != B.shape[0]:
        raise ValueError("Invalid shapes for matrix multiplication.")
    return A @ B


def transpose(A: Matrix) -> Matrix:
    """Transpose: A^T"""
    return A.T


# ---------------------------------------------------------------------
# Determinant & Inverse
# ---------------------------------------------------------------------

def determinant(A: Matrix) -> float:
    """
    det(A) — only valid for square matrices.
    """
    _validate_square(A)
    return float(np.linalg.det(A))


def inverse(A: Matrix) -> Matrix:
    """
    Compute A^{-1}.
    Exists iff det(A) ≠ 0.
    """
    _validate_square(A)

    if np.isclose(np.linalg.det(A), 0.0):
        raise ValueError("Matrix is singular; inverse does not exist.")

    return np.linalg.inv(A)


# ---------------------------------------------------------------------
# Rank
# ---------------------------------------------------------------------

def rank(A: Matrix) -> int:
    """
    Rank = number of linearly independent rows/columns.
    """
    return int(np.linalg.matrix_rank(A))


# ---------------------------------------------------------------------
# Eigen Decomposition
# ---------------------------------------------------------------------

def eigen_decomposition(A: Matrix) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute eigenvalues and eigenvectors.

    A v = λ v
    Only valid for square matrices.
    """
    _validate_square(A)
    vals, vecs = np.linalg.eig(A)
    return vals, vecs


# ---------------------------------------------------------------------
# Matrix Norm
# ---------------------------------------------------------------------

def matrix_norm(A: Matrix, ord: int | str = "fro") -> float:
    """
    Matrix norm.
    Default: Frobenius norm.
    """
    return float(np.linalg.norm(A, ord=ord))


# ---------------------------------------------------------------------
# Example Usage
# ---------------------------------------------------------------------

if __name__ == "__main__":
    A = np.array([[1, 2], [3, 4]], dtype=float)
    B = np.array([[5, 6], [7, 8]], dtype=float)

    print("Addition:\n - 02_matrices.py:136", add(A, B))
    print("Multiplication:\n - 02_matrices.py:137", multiply(A, B))
    print("Transpose:\n - 02_matrices.py:138", transpose(A))
    print("Determinant: - 02_matrices.py:139", determinant(A))
    print("Inverse:\n - 02_matrices.py:140", inverse(A))
    print("Rank: - 02_matrices.py:141", rank(A))

    vals, vecs = eigen_decomposition(A)
    print("Eigenvalues: - 02_matrices.py:144", vals)
    print("Eigenvectors:\n - 02_matrices.py:145", vecs)

    print("Frobenius Norm: - 02_matrices.py:147", matrix_norm(A))