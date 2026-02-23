"""
Moore–Penrose Pseudoinverse Utilities
Core tools for least squares, regression, and ML optimization.
"""

import numpy as np


# -------------------------------------------------
# Core Pseudoinverse Utilities
# -------------------------------------------------

def compute_pseudoinverse(A: np.ndarray, tol: float = 1e-12) -> np.ndarray:
    """
    Compute Moore–Penrose pseudoinverse using SVD.

    Args:
        A: Input matrix (m x n)
        tol: Singular value threshold for numerical stability

    Returns:
        A_pinv: Pseudoinverse of A
    """
    if A.ndim != 2:
        raise ValueError("Input must be a 2D matrix.")

    U, S, Vt = np.linalg.svd(A, full_matrices=False)

    # Invert only non-zero singular values
    S_inv = np.array([1/s if s > tol else 0.0 for s in S])
    Sigma_inv = np.diag(S_inv)

    return Vt.T @ Sigma_inv @ U.T


def least_squares_solution(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Solve overdetermined system Ax = b using pseudoinverse.

    Returns:
        x minimizing ||Ax - b||₂
    """
    A_pinv = compute_pseudoinverse(A)
    return A_pinv @ b


def pseudoinverse_via_normal_equation(A: np.ndarray) -> np.ndarray:
    """
    Compute pseudoinverse via normal equation:
        (AᵀA)⁻¹ Aᵀ
    Valid only if A has full column rank.
    """
    if A.ndim != 2:
        raise ValueError("Input must be 2D.")

    if np.linalg.matrix_rank(A) < A.shape[1]:
        raise ValueError("Matrix does not have full column rank.")

    return np.linalg.inv(A.T @ A) @ A.T


def verify_penrose_condition(A: np.ndarray, A_pinv: np.ndarray) -> bool:
    """
    Verify one Penrose condition: A A⁺ A = A
    """
    return np.allclose(A @ A_pinv @ A, A)


# -------------------------------------------------
# Example Usage
# -------------------------------------------------

if __name__ == "__main__":

    A = np.array([[1, 2],
                  [3, 4],
                  [5, 6]])

    b = np.array([7, 8, 9])

    A_pinv = compute_pseudoinverse(A)

    print("Pseudoinverse:\n - 10_pseudoinverse.py:83", A_pinv)

    x = least_squares_solution(A, b)
    print("Least Squares Solution:\n - 10_pseudoinverse.py:86", x)

    print("Penrose condition valid: - 10_pseudoinverse.py:88",
          verify_penrose_condition(A, A_pinv))

    # Only valid if full column rank
    if np.linalg.matrix_rank(A) == A.shape[1]:
        print("Normal Equation match: - 10_pseudoinverse.py:93",
              np.allclose(A_pinv,
                          pseudoinverse_via_normal_equation(A)))