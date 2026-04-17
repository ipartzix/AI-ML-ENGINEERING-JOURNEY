import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


def evaluate_model(model, X_test, y_test):
    """Evaluate a Keras model and print metrics."""
    y_pred = model.predict(X_test)
    if y_pred.shape[1] == 1:

        y_pred = (y_pred > 0.5).astype(int)
    print("Accuracy:", accuracy_score(y_test, y_pred))

    print("Classification Report:\n", classification_report(y_test, y_pred))
    plot_confusion(y_test, y_pred)


def plot_confusion(y_true, y_pred, figsize=(6, 6)):
    
    """Plot confusion matrix."""

    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=figsize)
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()
