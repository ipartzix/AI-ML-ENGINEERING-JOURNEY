"""
Angle Between Vectors & Cosine Similarity
Core utilities for ML / AI vector similarity operations.
"""

import numpy as np


# -------------------------------------------------
# Core Linear Algebra Utilities
# -------------------------------------------------

def dot_product(a: np.ndarray, b: np.ndarray) -> float:
    """
    Compute dot product of two vectors.
    """
    _validate_same_shape(a, b)
    return float(np.dot(a, b))


def vector_norm(v: np.ndarray) -> float:
    """
    Compute Euclidean (L2) norm of a vector.
    """
    return float(np.linalg.norm(v))


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """
    Compute cosine similarity between two vectors.

    Returns:
        float in [-1, 1]
    Raises:
        ValueError if any vector has zero magnitude.
    """
    _validate_same_shape(a, b)

    norm_a = vector_norm(a)
    norm_b = vector_norm(b)

    if norm_a == 0 or norm_b == 0:
        raise ValueError("Cosine similarity undefined for zero vector.")

    return dot_product(a, b) / (norm_a * norm_b)


def angle_between_vectors(a: np.ndarray, b: np.ndarray) -> float:
    """
    Compute angle (in radians) between two vectors.
    """
    cos_theta = cosine_similarity(a, b)
    return float(np.arccos(np.clip(cos_theta, -1.0, 1.0)))


# -------------------------------------------------
# Validation Helpers
# -------------------------------------------------

def _validate_same_shape(a: np.ndarray, b: np.ndarray):
    if a.shape != b.shape:
        raise ValueError("Vectors must have the same dimensions.")


# -------------------------------------------------
# Example Usage
# -------------------------------------------------

if __name__ == "__main__":

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    print("Dot Product: - 07_angle_similarity.py:74", dot_product(a, b))
    print("Cosine Similarity: - 07_angle_similarity.py:75", cosine_similarity(a, b))
    print("Angle (radians): - 07_angle_similarity.py:76", angle_between_vectors(a, b))

    # Orthogonal example
    v1 = np.array([1, 0])
    v2 = np.array([0, 1])

    print("Orthogonal Cosine: - 07_angle_similarity.py:82", cosine_similarity(v1, v2))