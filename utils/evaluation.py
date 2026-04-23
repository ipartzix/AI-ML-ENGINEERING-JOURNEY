import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


def _to_label_predictions(y_pred):
    y_pred = np.asarray(y_pred)

    if y_pred.ndim == 1:
        return y_pred

    if y_pred.ndim == 2 and y_pred.shape[1] == 1:
        return (y_pred.ravel() > 0.5).astype(int)

    if y_pred.ndim == 2:
        return np.argmax(y_pred, axis=1)

    raise ValueError("Unsupported prediction shape. Expected 1D or 2D predictions.")


def evaluate_model(model, X_test, y_test):
    """Evaluate a Keras model and print metrics."""
    y_true = np.asarray(y_test).ravel()
    y_pred = _to_label_predictions(model.predict(X_test)).ravel()

    print("Accuracy:", accuracy_score(y_true, y_pred))

    print("Classification Report:\n", classification_report(y_true, y_pred))
    plot_confusion(y_true, y_pred)


def plot_confusion(y_true, y_pred, figsize=(6, 6)):
    """Plot confusion matrix."""

    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=figsize)
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()
