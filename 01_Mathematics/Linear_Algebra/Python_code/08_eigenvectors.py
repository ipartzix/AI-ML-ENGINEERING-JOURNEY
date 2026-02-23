"""
Eigenvalues & Eigenvectors Utilities
Core linear algebra tools for PCA, transformations, and ML systems.
"""

import numpy as np


# -------------------------------------------------
# Validation
# -------------------------------------------------

def _validate_square_matrix(A: np.ndarray):
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("Matrix must be square.")


# -------------------------------------------------
# Core Eigen Utilities
# -------------------------------------------------

def compute_eigendecomposition(A: np.ndarray):
    """
    Compute eigenvalues and eigenvectors of a square matrix.

    Returns:
        eigenvalues (1D array)
        eigenvectors (columns correspond to eigenvectors)
    """
    _validate_square_matrix(A)
    values, vectors = np.linalg.eig(A)
    return values, vectors


def diagonalize_matrix(A: np.ndarray):
    """
    Diagonalize matrix A if possible.
    Returns:
        P, D, P_inv
    Raises:
        ValueError if matrix is not diagonalizable.
    """
    values, vectors = compute_eigendecomposition(A)

    if np.linalg.matrix_rank(vectors) < A.shape[0]:
        raise ValueError("Matrix is not diagonalizable (insufficient independent eigenvectors).")

    P = vectors
    D = np.diag(values)
    P_inv = np.linalg.inv(P)

    return P, D, P_inv


def verify_diagonalization(A: np.ndarray) -> bool:
    """
    Verify A = P D P⁻¹.
    """
    P, D, P_inv = diagonalize_matrix(A)
    return np.allclose(A, P @ D @ P_inv)


def trace_from_eigenvalues(A: np.ndarray) -> float:
    """
    Trace equals sum of eigenvalues.
    """
    values, _ = compute_eigendecomposition(A)
    return float(np.sum(values))


def determinant_from_eigenvalues(A: np.ndarray) -> float:
    """
    Determinant equals product of eigenvalues.
    """
    values, _ = compute_eigendecomposition(A)
    return float(np.prod(values))


# -------------------------------------------------
# Example Usage
# -------------------------------------------------

if __name__ == "__main__":

    A = np.array([[2, 1],
                  [1, 2]])

    eigenvalues, eigenvectors = compute_eigendecomposition(A)

    print("Eigenvalues:\n - 08_eigenvectors.py:90", eigenvalues)
    print("Eigenvectors:\n - 08_eigenvectors.py:91", eigenvectors)

    print("Diagonalization valid: - 08_eigenvectors.py:93", verify_diagonalization(A))
    print("Trace (from eigenvalues): - 08_eigenvectors.py:94", trace_from_eigenvalues(A))
    print("Determinant (from eigenvalues): - 08_eigenvectors.py:95", determinant_from_eigenvalues(A))