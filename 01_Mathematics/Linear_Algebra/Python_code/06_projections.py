"""
projections.py

Vector projection utilities for AI / Machine Learning.
All vectors assumed to be 1D NumPy arrays in R^n.
"""

from typing import Tuple
import numpy as np

Vector = np.ndarray
Matrix = np.ndarray


# ---------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------

def _validate_vector(x: Vector) -> None:
    if x.ndim != 1:
        raise ValueError("Input must be a 1D vector.")


def _validate_same_dimension(a: Vector, b: Vector) -> None:
    _validate_vector(a)
    _validate_vector(b)
    if a.shape[0] != b.shape[0]:
        raise ValueError(
            f"Dimension mismatch: {a.shape} vs {b.shape}"
        )


# ---------------------------------------------------------------------
# Scalar Projection
# ---------------------------------------------------------------------

def scalar_projection(a: Vector, b: Vector) -> float:
    """
    Scalar projection of a onto b:

        comp_b(a) = (a · b) / ||b||
    """
    _validate_same_dimension(a, b)

    norm_b = np.linalg.norm(b)
    if norm_b == 0:
        raise ValueError("Cannot project onto zero vector.")

    return float(np.dot(a, b) / norm_b)


# ---------------------------------------------------------------------
# Vector Projection
# ---------------------------------------------------------------------

def vector_projection(a: Vector, b: Vector) -> Vector:
    """
    Vector projection of a onto b:

        proj_b(a) = (a · b / b · b) b
    """
    _validate_same_dimension(a, b)

    denom = np.dot(b, b)
    if denom == 0:
        raise ValueError("Cannot project onto zero vector.")

    scalar = np.dot(a, b) / denom
    return scalar * b


# ---------------------------------------------------------------------
# Unit Vector
# ---------------------------------------------------------------------

def unit_vector(b: Vector) -> Vector:
    """
    Normalize vector:

        u = b / ||b||
    """
    _validate_vector(b)

    norm_b = np.linalg.norm(b)
    if norm_b == 0:
        raise ValueError("Zero vector cannot be normalized.")

    return b / norm_b


# ---------------------------------------------------------------------
# Projection Matrix
# ---------------------------------------------------------------------

def projection_matrix(X: Matrix) -> Matrix:
    """
    Projection matrix onto column space of X:

        P = X (X^T X)^(-1) X^T

    Used in least squares regression.
    """
    if X.ndim != 2:
        raise ValueError("Input must be 2D matrix.")

    XtX = X.T @ X

    if np.linalg.matrix_rank(XtX) < XtX.shape[0]:
        raise ValueError("X^T X is singular. Columns must be linearly independent.")

    return X @ np.linalg.inv(XtX) @ X.T


# ---------------------------------------------------------------------
# Least Squares Prediction
# ---------------------------------------------------------------------

def least_squares_projection(X: Matrix, y: Vector) -> Vector:
    """
    Compute projection of y onto column space of X:

        y_hat = P y
    """
    if X.shape[0] != y.shape[0]:
        raise ValueError("Row mismatch between X and y.")

    P = projection_matrix(X)
    return P @ y


# ---------------------------------------------------------------------
# Example Usage
# ---------------------------------------------------------------------

if __name__ == "__main__":
    a = np.array([3.0, 4.0])
    b = np.array([1.0, 0.0])

    print("Scalar Projection: - 06_projections.py:139", scalar_projection(a, b))
    print("Vector Projection: - 06_projections.py:140", vector_projection(a, b))

    b2 = np.array([3.0, 4.0])
    print("Unit Vector: - 06_projections.py:143", unit_vector(b2))

    X = np.array([[1.0], [2.0], [3.0]])
    y = np.array([2.0, 2.5, 3.0])
    print("Least Squares Prediction: - 06_projections.py:147", least_squares_projection(X, y))