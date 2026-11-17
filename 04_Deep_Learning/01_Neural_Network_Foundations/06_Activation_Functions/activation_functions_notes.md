# Activation Functions --- Deep Learning Notes

## 1. What is an Activation Function?

An **activation function** is a mathematical function applied to the
output of a neuron. It determines the neuron's final output, often
called its *activation*.

A neuron first calculates a weighted sum of its inputs and adds a bias:

\[ z = `\sum`{=tex}\_{i=1}\^{n} w_i x_i + b \]

Then it applies an activation function:

\[ a = f(z) \]

Where:

-   (x_i): input features
-   (w_i): weights learned during training
-   (b): bias
-   (z): weighted sum before activation (pre-activation)
-   (f): activation function
-   (a): output after activation

In short, the activation function transforms a neuron's pre-activation
value into its output.

## 2. Why Do We Need Activation Functions?

The most important reason is **non-linearity**.

Real-world patterns are often non-linear. A neural network needs to
learn relationships that cannot be represented by a simple straight line
or linear transformation.

Consider a network containing several layers. If every layer uses only a
linear transformation, stacking those layers still produces one overall
linear transformation:

\[ W_2(W_1x+b_1)+b_2 = W'x+b' \]

Therefore, adding more linear layers without a non-linear activation
does not give the network the ability to learn more complex non-linear
relationships.

A non-linear activation function allows a neural network to learn
complex patterns and decision boundaries.

### Key points

-   Activation functions introduce non-linearity into neural networks.
-   They help networks learn complex relationships in data.
-   They influence gradient flow during backpropagation.
-   Their output range and mathematical properties affect training
    behaviour.
-   The appropriate activation depends on the layer and the task.

## 3. Common Activation Functions

### 3.1 Binary Step Function

The binary step function returns either 0 or 1 depending on whether the
input crosses a threshold.

\[ f(x) =
```{=tex}
\begin{cases}
0 & x < 0 \\
1 & x \geq 0
\end{cases}
```
\]

**Output range:** ({0,1})

**Advantages** - Simple threshold-based decision. - Historically useful
for understanding early perceptrons.

**Limitations** - Its derivative is zero almost everywhere and undefined
at the threshold. - It cannot provide useful gradients for
gradient-based training.

**Typical use:** Historical perceptron models and conceptual
demonstrations; not commonly used as a hidden-layer activation in modern
deep networks.

### 3.2 Linear Activation

The linear activation returns the input unchanged, or scales it by a
constant.

\[ f(x)=x \]

**Output range:** ((-`\infty`{=tex},+`\infty`{=tex}))

**Advantages** - Simple. - Preserves the numerical scale of the input.

**Limitations** - It does not introduce non-linearity. - A network made
entirely of linear layers remains equivalent to a single linear
transformation.

**Typical use:** Commonly used in the output layer of regression models
when predictions can take any real value.

### 3.3 Sigmoid Activation

The sigmoid function maps any real-valued input to a value between 0 and
1.

\[ `\sigma`{=tex}(x)=`\frac{1}{1+e^{-x}}`{=tex} \]

**Output range:** ((0,1))

**Advantages** - Produces values that can be interpreted as
probabilities in suitable binary-classification models. - Smooth and
differentiable. - Historically common in neural networks.

**Limitations** - Can suffer from the **vanishing gradient problem** for
very large positive or negative inputs. - Its outputs are not
zero-centred. - Exponentiation can be less computationally efficient
than simpler activations.

**Typical use:** Output layer for binary classification, usually when
paired with binary cross-entropy loss. In practice, use a numerically
stable logits-based loss when possible.

### 3.4 Tanh (Hyperbolic Tangent)

The tanh function maps real-valued inputs to values between -1 and 1.

\[ `\tanh`{=tex}(x)=`\frac{e^x-e^{-x}}{e^x+e^{-x}}`{=tex} \]

**Output range:** ((-1,1))

**Advantages** - Zero-centred output. - Smooth and differentiable. -
Often provides more balanced activations than sigmoid because its output
includes negative values.

**Limitations** - Can suffer from vanishing gradients for inputs with
large absolute values.

**Typical use:** Some recurrent neural network components and models
where zero-centred activations are useful.

### 3.5 ReLU (Rectified Linear Unit)

ReLU outputs zero for negative inputs and returns the input for
non-negative inputs.

\[ f(x)=`\max`{=tex}(0,x) \]

**Output range:** (\[0,+`\infty`{=tex}))

**Advantages** - Simple and computationally efficient. - Helps reduce
the vanishing-gradient issue for positive inputs. - Often leads to
sparse activations because negative inputs become zero. - A common
default for hidden layers in many feed-forward networks and CNNs.

**Limitations** - Can produce **dying ReLU** neurons: a neuron may get
stuck outputting zero if it receives negative inputs and stops receiving
useful gradients. - Not zero-centred.

**Typical use:** Hidden layers in many standard neural networks and
convolutional neural networks.

### 3.6 Leaky ReLU

Leaky ReLU allows a small, non-zero output for negative inputs.

\[ f(x)=
```{=tex}
\begin{cases}
x & x \geq 0 \\
\alpha x & x < 0
\end{cases}
```
\]

Here, (`\alpha`{=tex}) is a small positive constant, often 0.01.

**Output range:** ((-`\infty`{=tex},+`\infty`{=tex}))

**Advantages** - Keeps a small gradient for negative inputs. - Can
reduce the dying ReLU problem.

**Limitations** - The negative slope (`\alpha`{=tex}) is a
hyperparameter. - It is not guaranteed to outperform ReLU.

**Typical use:** Hidden layers when a non-zero negative-side gradient is
desired.

### 3.7 PReLU (Parametric ReLU)

PReLU is similar to Leaky ReLU, but its negative slope is learned during
training.

\[ f(x)=
```{=tex}
\begin{cases}
x & x \geq 0 \\
\alpha x & x < 0
\end{cases}
```
\]

Unlike Leaky ReLU, (`\alpha`{=tex}) is a trainable parameter.

**Advantages** - The model can learn the negative slope from data. -
Provides a non-zero gradient for negative inputs.

**Limitations** - Adds trainable parameters. - May overfit in some
settings, especially with limited data.

**Typical use:** Some deep vision architectures and experiments where
learning the negative slope is useful.

### 3.8 ELU (Exponential Linear Unit)

ELU is linear for positive inputs and exponential for negative inputs.

\[ f(x)=
```{=tex}
\begin{cases}
x & x > 0 \\
\alpha(e^x-1) & x \leq 0
\end{cases}
```
\]

Here, (`\alpha`{=tex}) controls the negative saturation value.

**Advantages** - Allows negative outputs. - Can produce activations
closer to zero-centred values. - Has a smooth negative region.

**Limitations** - More computationally expensive than ReLU because it
uses an exponential. - Its benefits depend on the model and training
setup.

**Typical use:** Alternative hidden-layer activation in some
feed-forward networks.

### 3.9 GELU (Gaussian Error Linear Unit)

GELU weights the input by its probability under a Gaussian distribution.

\[ `\operatorname{GELU}`{=tex}(x)=x`\Phi`{=tex}(x) \]

Here, (`\Phi`{=tex}(x)) is the cumulative distribution function of the
standard normal distribution.

A commonly used approximation is:

\[ `\operatorname{GELU}`{=tex}(x)`\approx`{=tex}
0.5x`\left`{=tex}(1+`\tanh`{=tex}`\left[\sqrt{\frac{2}{\pi}}(x+0.044715x^3)\right]`{=tex}`\right`{=tex})
\]

**Advantages** - Smooth activation. - Gradually suppresses negative
inputs rather than setting all of them exactly to zero. - Works well in
many Transformer architectures.

**Limitations** - More computationally involved than ReLU. - The best
choice depends on the architecture and implementation.

**Typical use:** Transformer models, including many BERT-style
architectures.

### 3.10 Softmax Activation

Softmax converts a vector of scores (logits) into a probability
distribution.

For class (i):

\[ `\operatorname{softmax}`{=tex}(z_i)=
`\frac{e^{z_i}}{\sum_{j=1}^{K}e^{z_j}}`{=tex} \]

Where: - (z_i): logit for class (i) - (K): number of classes - The
output values lie between 0 and 1. - All output values sum to 1.

**Advantages** - Converts multiple class scores into a normalized
distribution. - Useful for mutually exclusive multiclass classification.

**Limitations** - Can be numerically unstable if implemented naively;
practical implementations use a stable formulation. - It is not
generally the right output activation for multilabel classification,
where classes are independent.

**Typical use:** Output layer for mutually exclusive multiclass
classification, commonly paired with categorical cross-entropy or a
logits-based cross-entropy loss.

## 4. Quick Comparison Table

  ------------------------------------------------------------------------------------------
  Activation                                Output range Main               Common use
                                                         characteristic     
  ---------------- ------------------------------------- ------------------ ----------------
  Binary Step                                     0 or 1 Hard threshold     Historical
                                                                            perceptrons

  Linear             ((-`\infty`{=tex},+`\infty`{=tex})) Identity mapping   Regression
                                                                            output

  Sigmoid                                         (0, 1) Probability-like   Binary
                                                         scalar output      classification
                                                                            output

  Tanh                                           (-1, 1) Zero-centred       Some RNN
                                                         output             components

  ReLU                                          \[0, +∞) Simple             Hidden layers
                                                         positive-side      
                                                         linearity          

  Leaky ReLU         ((-`\infty`{=tex},+`\infty`{=tex})) Small              Hidden layers
                                                         negative-side      
                                                         slope              

  PReLU              ((-`\infty`{=tex},+`\infty`{=tex})) Learnable negative Some deep
                                                         slope              networks

  ELU                ((-`\alpha`{=tex},+`\infty`{=tex})) Exponential        Alternative
                                                         negative side      hidden layers

  GELU                                     Approximately Smooth             Transformers
                     ((-`\infty`{=tex},+`\infty`{=tex})) input-dependent    
                                                         gating             

  Softmax                               (0, 1) per class Outputs sum to 1   Multiclass
                                                                            output
  ------------------------------------------------------------------------------------------

## 5. Which Activation Function Should You Choose?

There is no single activation function that is best for every neural
network. The choice depends on the architecture, output format, loss
function, and task.

  -----------------------------------------------------------------------
  Network component /     Common choice           Reason
  task                                            
  ----------------------- ----------------------- -----------------------
  Hidden layers in a      ReLU                    Efficient and widely
  basic MLP                                       used

  Hidden layers when      Leaky ReLU or PReLU     Retains a negative-side
  avoiding zero                                   gradient
  negative-side gradients                         

  Some Transformer        GELU or a gated         Common in modern
  feed-forward blocks     activation such as      Transformer designs
                          SwiGLU                  

  Binary classification   Sigmoid                 Produces one value
  output                                          between 0 and 1

  Mutually exclusive      Softmax                 Produces a normalized
  multiclass output                               class distribution

  Regression output       Linear                  Allows unrestricted
                                                  real-valued predictions
  -----------------------------------------------------------------------

**Important:** Some frameworks combine the output activation and loss
internally. For example, a binary-cross-entropy-with-logits loss expects
raw logits, not sigmoid probabilities. Similarly, a
softmax-cross-entropy-with-logits loss expects raw class scores. Follow
the loss function's input requirements to avoid applying an activation
twice.

## 6. Activation Functions and Backpropagation

Neural networks are trained using gradient-based optimization. During
backpropagation, gradients pass through activation functions according
to the chain rule.

For a neuron:

\[ a=f(z) \]

The gradient with respect to the pre-activation value includes:

\[ `\frac{\partial a}{\partial z}`{=tex}=f'(z) \]

The derivative of an activation function therefore affects how much
gradient is passed backward.

### Vanishing gradients

For sigmoid and tanh, the derivative becomes very small when the input
is far into the saturated regions. When many such derivatives are
multiplied across layers, gradients can become extremely small. Earlier
layers then learn very slowly.

### Dying ReLU

For negative inputs, standard ReLU has a derivative of zero. If a neuron
consistently receives negative inputs, it may stop updating and remain
inactive. Leaky ReLU and PReLU retain a small negative-side gradient.

### Practical lesson

Activation choice affects optimization, but it is not the only factor.
Initialization, normalization, architecture, learning rate, data, and
loss function also influence gradient flow and training stability.

## 7. NumPy Implementations

The following examples implement common activation functions using
NumPy.

``` python
import numpy as np


def binary_step(x):
    return np.where(x >= 0, 1, 0)


def linear(x):
    return x


def sigmoid(x):
    # Clip values to reduce overflow in exp for this simple example.
    x = np.clip(x, -500, 500)
    return 1 / (1 + np.exp(-x))


def tanh(x):
    return np.tanh(x)


def relu(x):
    return np.maximum(0, x)


def leaky_relu(x, alpha=0.01):
    return np.where(x >= 0, x, alpha * x)


def prelu(x, alpha=0.25):
    return np.where(x >= 0, x, alpha * x)


def elu(x, alpha=1.0):
    return np.where(x > 0, x, alpha * (np.exp(x) - 1))


def gelu_approx(x):
    return 0.5 * x * (
        1 + np.tanh(
            np.sqrt(2 / np.pi) * (x + 0.044715 * x**3)
        )
    )


def softmax(x):
    # Subtract max for numerical stability.
    shifted = x - np.max(x, axis=-1, keepdims=True)
    exp_values = np.exp(shifted)
    return exp_values / np.sum(exp_values, axis=-1, keepdims=True)


values = np.array([-2.0, -1.0, 0.0, 1.0, 2.0])

print("Binary step:", binary_step(values))
print("Linear:", linear(values))
print("Sigmoid:", sigmoid(values))
print("Tanh:", tanh(values))
print("ReLU:", relu(values))
print("Leaky ReLU:", leaky_relu(values))
print("PReLU:", prelu(values))
print("ELU:", elu(values))
print("GELU:", gelu_approx(values))

logits = np.array([2.0, 1.0, 0.1])
print("Softmax:", softmax(logits))
```

**Note:** These are educational implementations. Deep-learning
frameworks provide optimized and numerically stable implementations for
production training.

## 8. Interview Questions and Answers

### Q1. What is an activation function?

An activation function transforms a neuron's pre-activation value into
its output. It commonly introduces non-linearity into a neural network.

### Q2. Why do neural networks need non-linear activation functions?

Without non-linear activations, a stack of linear layers is
mathematically equivalent to one linear transformation. Non-linear
activations allow the network to learn complex patterns.

### Q3. Why is ReLU widely used?

ReLU is computationally simple, produces sparse activations for negative
inputs, and has a constant gradient for positive inputs.

### Q4. What is the vanishing gradient problem?

It occurs when gradients become extremely small as they are propagated
backward through a network. Earlier layers then receive very small
updates and may learn slowly.

### Q5. Why can sigmoid cause vanishing gradients?

For very large positive or negative inputs, sigmoid saturates near 1 or
0. Its derivative becomes close to zero in those regions.

### Q6. What is the dying ReLU problem?

A ReLU neuron can become inactive when it consistently receives negative
inputs. Since the gradient is zero on the negative side, the neuron may
stop learning.

### Q7. What is the difference between ReLU and Leaky ReLU?

ReLU returns zero for negative inputs. Leaky ReLU returns a small
negative value proportional to the input, preserving a small gradient on
the negative side.

### Q8. What is the difference between sigmoid and softmax?

Sigmoid independently maps each input to a value between 0 and 1.
Softmax converts a vector of class scores into values that sum to 1.
Sigmoid is common for binary or multilabel outputs; softmax is common
for mutually exclusive multiclass outputs.

### Q9. Why is linear activation used in regression output layers?

A linear output is not restricted to a fixed interval, so the model can
predict any real-valued target.

### Q10. Why is GELU used in many Transformers?

GELU is a smooth activation that works well in many Transformer
feed-forward blocks. Its use is an architectural choice, not a universal
requirement.

## 9. Key Takeaways

1.  An activation function is applied to a neuron's weighted sum plus
    bias.
2.  Non-linear activations enable neural networks to learn non-linear
    relationships.
3.  ReLU is a common default for hidden layers in many standard
    networks.
4.  Sigmoid is commonly used for a single binary-classification output.
5.  Softmax is commonly used for mutually exclusive multiclass
    classification.
6.  Linear activation is commonly used for unrestricted regression
    outputs.
7.  Sigmoid and tanh can suffer from vanishing gradients in saturated
    regions.
8.  ReLU can suffer from the dying ReLU problem.
9.  GELU is common in Transformer architectures.
10. Always check the expected inputs of the loss function: some losses
    expect logits rather than activated probabilities.

## 10. Self-Test Quiz

Try answering these questions before checking the answers.

1.  What is the main reason activation functions are used in neural
    networks?
2.  Which activation function is commonly used in the hidden layers of a
    basic MLP?
3.  Which activation function maps values into the range (0, 1)?
4.  Which activation function is commonly used for mutually exclusive
    multiclass classification?
5.  What is the dying ReLU problem?

### Answers

1.  To introduce non-linearity so the network can learn complex
    relationships.
2.  ReLU is a common choice.
3.  Sigmoid.
4.  Softmax.
5.  A ReLU neuron can become inactive when it consistently receives
    negative inputs and therefore receives zero gradient.

------------------------------------------------------------------------

## Suggested Further Study

After understanding activation functions:

1.  Study derivatives of sigmoid, tanh, and ReLU.
2.  Derive how activation derivatives appear in the backpropagation
    chain rule.
3.  Implement a small neural network and compare ReLU, sigmoid, and
    tanh.
4.  Observe training loss and validation performance rather than
    assuming one activation is always best.
5.  Learn how logits-based loss functions work in PyTorch or TensorFlow.

*These notes are intended as a conceptual and practical reference.
Activation selection should be validated for the specific model and
dataset.*
