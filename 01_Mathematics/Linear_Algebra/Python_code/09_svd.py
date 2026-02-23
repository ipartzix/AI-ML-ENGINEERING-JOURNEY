"""
Singular Value Decomposition (SVD) Utilities
Core tools for dimensionality reduction, compression, and ML pipelines.
"""

import numpy as np


# -------------------------------------------------
# Core SVD Utilities
# -------------------------------------------------

def compute_svd(A: np.ndarray, full_matrices: bool = False):
    """
    Compute Singular Value Decomposition.

    Args:
        A: Input matrix (m x n)
        full_matrices: Whether to compute full or reduced SVD

    Returns:
        U, S, Vt
    """
    if A.ndim != 2:
        raise ValueError("Input must be a 2D matrix.")

    U, S, Vt = np.linalg.svd(A, full_matrices=full_matrices)
    return U, S, Vt


def reconstruct_matrix(U: np.ndarray, S: np.ndarray, Vt: np.ndarray) -> np.ndarray:
    """
    Reconstruct matrix from SVD components.
    """
    return U @ np.diag(S) @ Vt


def matrix_rank_from_svd(S: np.ndarray, tol: float = 1e-10) -> int:
    """
    Compute matrix rank from singular values.
    """
    return int(np.sum(S > tol))


def low_rank_approximation(A: np.ndarray, k: int):
    """
    Compute rank-k approximation using truncated SVD.

    Args:
        A: Input matrix
        k: Target rank (k <= min(m, n))

    Returns:
        Ak: Rank-k approximation
    """
    U, S, Vt = compute_svd(A)

    max_rank = min(A.shape)
    if k > max_rank:
        raise ValueError(f"k must be ≤ {max_rank}")

    U_k = U[:, :k]
    S_k = S[:k]
    Vt_k = Vt[:k, :]

    return U_k @ np.diag(S_k) @ Vt_k


def singular_values_from_eigen(A: np.ndarray):
    """
    Compute singular values via eigenvalues of AᵀA.
    (Educational use only — less stable than direct SVD.)
    """
    eigvals = np.linalg.eigvals(A.T @ A)
    return np.sqrt(np.maximum(eigvals, 0))


# -------------------------------------------------
# Example Usage
# -------------------------------------------------

if __name__ == "__main__":

    A = np.array([[3, 1, 1],
                  [-1, 3, 1]])

    U, S, Vt = compute_svd(A)

    print("Singular Values:\n - 09_svd.py:89", S)
    print("Rank (from SVD): - 09_svd.py:90", matrix_rank_from_svd(S))

    A_reconstructed = reconstruct_matrix(U, S, Vt)
    print("Reconstruction valid: - 09_svd.py:93", np.allclose(A, A_reconstructed))

    # Rank-1 approximation
    Ak = low_rank_approximation(A, k=1)
    print("Rank1 Approximation:\n - 09_svd.py:97", Ak)

    # Educational check
    print("Singular values via eigen: - 09_svd.py:100", singular_values_from_eigen(A))