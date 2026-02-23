"""
Principal Component Analysis (PCA) from Scratch
Numerically stable and reusable implementation.
"""

import numpy as np


class PCA:
    """
    Principal Component Analysis implementation.
    """

    def __init__(self, n_components: int, method: str = "svd"):
        """
        Args:
            n_components: number of principal components
            method: "svd" (recommended) or "eigen"
        """
        if n_components <= 0:
            raise ValueError("n_components must be positive.")

        if method not in ("svd", "eigen"):
            raise ValueError("method must be 'svd' or 'eigen'.")

        self.n_components = n_components
        self.method = method

        self.mean_ = None
        self.components_ = None
        self.explained_variance_ = None
        self.explained_variance_ratio_ = None

    # -------------------------------------------------
    # Fit
    # -------------------------------------------------

    def fit(self, X: np.ndarray):
        """
        Fit PCA to dataset.
        """
        if X.ndim != 2:
            raise ValueError("Input must be 2D array.")

        n_samples, n_features = X.shape

        if self.n_components > n_features:
            raise ValueError("n_components cannot exceed number of features.")

        # Mean centering
        self.mean_ = np.mean(X, axis=0)
        X_centered = X - self.mean_

        if self.method == "eigen":
            self._fit_eigen(X_centered)
        else:
            self._fit_svd(X_centered)

        return self

    def _fit_eigen(self, X_centered: np.ndarray):
        """
        PCA via covariance eigen decomposition.
        """
        cov_matrix = np.cov(X_centered, rowvar=False)

        # Use eigh for symmetric matrices (more stable)
        eig_vals, eig_vecs = np.linalg.eigh(cov_matrix)

        # Sort descending
        idx = np.argsort(eig_vals)[::-1]
        eig_vals = eig_vals[idx]
        eig_vecs = eig_vecs[:, idx]

        self.components_ = eig_vecs[:, :self.n_components]
        self.explained_variance_ = eig_vals[:self.n_components]
        self.explained_variance_ratio_ = (
            eig_vals / np.sum(eig_vals)
        )[:self.n_components]

    def _fit_svd(self, X_centered: np.ndarray):
        """
        PCA via SVD (recommended).
        """
        U, S, Vt = np.linalg.svd(X_centered, full_matrices=False)

        self.components_ = Vt[:self.n_components].T

        # Variance explained
        eigenvalues = (S ** 2) / (X_centered.shape[0] - 1)
        self.explained_variance_ = eigenvalues[:self.n_components]
        self.explained_variance_ratio_ = (
            eigenvalues / np.sum(eigenvalues)
        )[:self.n_components]

    # -------------------------------------------------
    # Transform
    # -------------------------------------------------

    def transform(self, X: np.ndarray) -> np.ndarray:
        """
        Project data onto principal components.
        """
        if self.components_ is None:
            raise ValueError("Model must be fitted first.")

        X_centered = X - self.mean_
        return X_centered @ self.components_

    def fit_transform(self, X: np.ndarray) -> np.ndarray:
        """
        Fit PCA and return projected data.
        """
        self.fit(X)
        return self.transform(X)

    def inverse_transform(self, X_transformed: np.ndarray) -> np.ndarray:
        """
        Reconstruct data from principal components.
        """
        return X_transformed @ self.components_.T + self.mean_


# -------------------------------------------------
# Example Usage
# -------------------------------------------------

if __name__ == "__main__":

    X = np.array([[2.5, 2.4],
                  [0.5, 0.7],
                  [2.2, 2.9],
                  [1.9, 2.2],
                  [3.1, 3.0],
                  [2.3, 2.7],
                  [2.0, 1.6],
                  [1.0, 1.1],
                  [1.5, 1.6],
                  [1.1, 0.9]])

    pca = PCA(n_components=1, method="svd")

    X_reduced = pca.fit_transform(X)

    print("Projected Data (first 5 rows):\n - 11_pca_from_scratch.py:145", X_reduced[:5])
    print("Explained Variance Ratio: - 11_pca_from_scratch.py:146", pca.explained_variance_ratio_)