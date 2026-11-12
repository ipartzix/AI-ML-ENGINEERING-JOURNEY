# Multilayer Perceptron (MLP)

## 1. What Is an MLP?

A **Multilayer Perceptron (MLP)** is a feed-forward artificial neural network made of interconnected neurons arranged in layers. It learns relationships between input features and target outputs by adjusting weights and biases during training.

Uses:
- **Classification:** predict a class or category.
- **Regression:** predict a continuous value.

## 2. MLP Architecture

An MLP typically contains:
1. **Input layer:** receives input features.
2. **Hidden layer(s):** learn intermediate representations.
3. **Output layer:** produces the prediction.

A fully connected (dense) layer connects each neuron to every neuron in the previous layer.

```text
Input Layer       Hidden Layer       Output Layer
 x₁ ─────┐
 x₂ ─────┼──────►  h₁ ─────┐
 x₃ ─────┘         h₂ ─────┼──────► ŷ
                    h₃ ─────┘
```

## 3. Artificial Neuron

A neuron calculates a weighted sum plus bias, then applies an activation function:

`z = Σ(wᵢxᵢ) + b`

`a = f(z)`

- `xᵢ`: input feature or previous-layer activation
- `wᵢ`: learnable weight
- `b`: learnable bias
- `f`: activation function
- `a`: neuron output (activation)

## 4. Forward Propagation

Forward propagation passes input data through the network to produce a prediction.

For layer `l`:

`z[l] = W[l]a[l−1] + b[l]`

`a[l] = f[l](z[l])`

For the input layer, `a[0] = x`.

Steps:
1. Input features enter the network.
2. Each layer computes a weighted sum plus bias.
3. The activation function transforms the result.
4. The final layer produces the prediction.

## 5. Why Activation Functions Matter

Without nonlinear activation functions, stacking dense layers is equivalent to a single linear transformation. The network would not learn general nonlinear relationships.

| Function | Typical use | Key point |
|---|---|---|
| ReLU | Hidden layers | `max(0, z)`; simple and efficient |
| Sigmoid | Binary output | Maps values to `(0, 1)` |
| Softmax | Multiclass output | Converts logits into class probabilities |
| Tanh | Some hidden layers | Maps values to `(-1, 1)` |

Choose activations based on the task and output representation.

## 6. Output Layer and Loss Function

| Task | Typical output | Common loss |
|---|---|---|
| Binary classification | One logit; sigmoid used to interpret probability | Binary cross-entropy |
| Multiclass, single-label classification | One logit per class; softmax for probabilities | Cross-entropy |
| Regression | One or more continuous values | MSE or MAE |

In PyTorch, `BCEWithLogitsLoss` accepts raw logits and handles sigmoid internally. `CrossEntropyLoss` typically expects raw logits, not softmax probabilities.

## 7. Loss Function

The loss measures the difference between a prediction and its target. A simplified average objective over `N` examples is:

`J(θ) = (1/N) Σ L(ŷᵢ, yᵢ)`

`θ` represents the trainable weights and biases. Training aims to reduce this objective.

## 8. Backpropagation

**Backpropagation** calculates gradients of the loss with respect to network parameters using the chain rule. It works backward from the output layer toward earlier layers to determine how each parameter contributed to the loss.

Backpropagation computes gradients; it does not itself update parameters. An optimizer uses the gradients to perform updates.

## 9. Gradient Descent and Optimizers

A basic gradient descent update is:

`θ ← θ − η∇θJ(θ)`

- `θ`: weights and biases
- `η`: learning rate
- `∇θJ`: gradient of the objective

Common optimizers:
- **SGD:** updates parameters using gradients from batches.
- **Momentum:** smooths updates using a running direction.
- **Adam:** adapts update sizes using running estimates of gradient moments.

## 10. MLP Training Workflow

```text
Prepare input and target data
          ↓
Initialize weights and biases
          ↓
Forward propagation
          ↓
Calculate loss
          ↓
Backpropagation (calculate gradients)
          ↓
Optimizer updates parameters
          ↓
Repeat over batches and epochs
          ↓
Evaluate on validation/test data
```

- **Batch:** examples processed together.
- **Epoch:** one pass through the training dataset.
- **Learning rate:** controls the size of optimizer updates.

## 11. Important Hyperparameters

| Hyperparameter | What it controls |
|---|---|
| Number of hidden layers | Network depth |
| Neurons per layer | Layer width/capacity |
| Learning rate | Update size |
| Batch size | Examples per update |
| Number of epochs | Training passes |
| Activation function | Nonlinear transformation |
| Optimizer | Parameter-update method |
| Regularization / weight decay | Helps control overfitting |

More layers or neurons do not automatically mean better performance. Evaluate capacity on validation data.

## 12. Overfitting and Regularization

An MLP can overfit when it learns training-specific patterns that do not generalize.

Ways to reduce overfitting:
- **L2 regularization / weight decay**
- **Dropout**
- **Early stopping** based on validation performance
- More representative training data
- Appropriate network size

Compare training and validation metrics to identify possible overfitting.

## 13. Strengths and Limitations

**Strengths**
- Learns nonlinear relationships.
- Supports classification and regression.
- Works with many fixed-size feature vectors.
- Builds foundational understanding for deeper neural networks.

**Limitations**
- Often benefits from feature scaling.
- Can overfit small datasets.
- Performance depends on architecture and hyperparameters.
- Does not exploit spatial or sequence structure as naturally as specialized architectures such as CNNs or Transformers.

## 14. MLP vs Single-Layer Perceptron

| Single-layer perceptron | MLP |
|---|---|
| No hidden layer in the standard form | One or more hidden layers |
| Learns a linear decision boundary | Nonlinear activations enable nonlinear boundaries |
| Classical form is limited to linearly separable classification | Can learn more complex nonlinear mappings |
| Uses a simple perceptron learning rule | Commonly trained using backpropagation and gradient-based optimizers |

## 15. Minimal PyTorch Example

This example builds an MLP for binary classification. `input_dim` must match the number of input features.

```python
import torch
from torch import nn

class MLP(nn.Module):
    def __init__(self, input_dim: int):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 1)  # One raw logit
        )

    def forward(self, x):
        return self.network(x)

model = MLP(input_dim=10)
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

# Example batch: 32 samples, 10 features each
x = torch.randn(32, 10)
y = torch.randint(0, 2, (32, 1)).float()

logits = model(x)
loss = criterion(logits, y)

optimizer.zero_grad()
loss.backward()
optimizer.step()

print(f"Loss: {loss.item():.4f}")
```

Notes:
- The final layer returns logits; do not apply sigmoid before `BCEWithLogitsLoss`.
- Targets are floats with values 0 or 1 and the same shape as logits.
- This is one training step, not a complete training pipeline.
- With real data, split data properly, fit preprocessing only on training data, and monitor validation performance.

## 16. Interview Questions

**1. What is an MLP?**  
A feed-forward neural network with an input layer, one or more hidden layers, and an output layer.

**2. Why are nonlinear activations needed?**  
Without them, multiple dense layers collapse into an equivalent linear transformation.

**3. What is forward propagation?**  
Computing activations layer by layer to obtain a prediction.

**4. What is backpropagation?**  
Using the chain rule to calculate gradients of the loss with respect to parameters.

**5. Are backpropagation and gradient descent the same?**  
No. Backpropagation calculates gradients; an optimizer uses them to update parameters.

**6. What happens if the learning rate is too high?**  
Training may oscillate or diverge. If too low, training can be very slow.

**7. Why use ReLU in hidden layers?**  
It is computationally simple and introduces nonlinearity, though it can produce inactive neurons.

**8. How can you detect overfitting?**  
Training performance improves while validation performance stalls or worsens.

**9. Can an MLP be used for regression?**  
Yes. Use a suitable output layer and a regression loss such as MSE or MAE.

**10. Why scale input features?**  
Very different feature scales can make optimization less effective and slow training.

## 17. Final Mental Model

- **Architecture:** layers of connected neurons.
- **Forward propagation:** produces predictions.
- **Loss:** measures prediction error.
- **Backpropagation:** calculates gradients.
- **Optimizer:** updates weights and biases.
- **Validation:** checks generalization and guides model selection.

**In one sentence:** An MLP learns a mapping from inputs to outputs by making predictions, measuring loss, calculating gradients through backpropagation, and updating parameters with an optimizer.
