"""
Rank & Linear Independence Utilities
Core tools for ML feature validation and matrix diagnostics.
"""

import numpy as np


# -------------------------------------------------
# Core Rank Utilities
# -------------------------------------------------

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    """
    Compute matrix rank using SVD-based numerical stability.
    """
    if A.ndim != 2:
        raise ValueError("Input must be a 2D matrix.")

    U, S, Vt = np.linalg.svd(A, full_matrices=False)
    return int(np.sum(S > tol))


def is_full_rank(A: np.ndarray) -> bool:
    """
    Check if matrix is full rank.
    """
    return matrix_rank(A) == min(A.shape)


def has_full_column_rank(A: np.ndarray) -> bool:
    """
    Check full column rank (rank = number of columns).
    """
    return matrix_rank(A) == A.shape[1]


def has_full_row_rank(A: np.ndarray) -> bool:
    """
    Check full row rank (rank = number of rows).
    """
    return matrix_rank(A) == A.shape[0]


# -------------------------------------------------
# Linear Independence Utilities
# -------------------------------------------------

def are_vectors_linearly_independent(*vectors: np.ndarray) -> bool:
    """
    Check if given vectors are linearly independent.
    """
    if len(vectors) == 0:
        raise ValueError("At least one vector required.")

    stacked = np.column_stack(vectors)
    return matrix_rank(stacked) == len(vectors)


def dependency_info(*vectors: np.ndarray):
    """
    Provide rank and independence diagnostics.
    """
    stacked = np.column_stack(vectors)
    rank = matrix_rank(stacked)
    return {
        "rank": rank,
        "num_vectors": len(vectors),
        "independent": rank == len(vectors),
    }


# -------------------------------------------------
# Determinant & Invertibility
# -------------------------------------------------

def is_invertible(A: np.ndarray) -> bool:
    """
    A square matrix is invertible iff full rank.
    """
    if A.shape[0] != A.shape[1]:
        return False

    return matrix_rank(A) == A.shape[0]


def determinant(A: np.ndarray) -> float:
    """
    Compute determinant (only valid for square matrices).
    """
    if A.shape[0] != A.shape[1]:
        raise ValueError("Determinant defined only for square matrices.")

    return float(np.linalg.det(A))


# -------------------------------------------------
# Example Usage
# -------------------------------------------------

if __name__ == "__main__":

    A = np.array([[1, 2, 3],
                  [2, 4, 6],
                  [1, 1, 1]])

    print("Rank(A): - 12_rank_independence.py:107", matrix_rank(A))
    print("Full rank: - 12_rank_independence.py:108", is_full_rank(A))

    v1 = np.array([1, 2])
    v2 = np.array([2, 4])

    print("Independent vectors: - 12_rank_independence.py:113",
          are_vectors_linearly_independent(v1, v2))

    B = np.eye(3)

    print("Invertible: - 12_rank_independence.py:118", is_invertible(B))
    print("Determinant: - 12_rank_independence.py:119", determinant(B))