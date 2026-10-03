# Deep Learning --- Complete Notes

> **Purpose:** A practical Deep Learning reference for an AI/ML
> Engineering learning path.\
> **Primary framework:** PyTorch\
> **Roadmap position:** Core ML → Deep Learning → Transformers → LLMs

------------------------------------------------------------------------

## 1. What Is Deep Learning?

**Deep Learning (DL)** is a subset of Machine Learning that uses neural
networks with multiple layers to learn hierarchical representations of
data.

Instead of manually designing every feature, a deep neural network can
learn increasingly complex representations from raw or processed inputs.

### Deep Learning vs Machine Learning

  -----------------------------------------------------------------------
  Aspect                  Traditional ML          Deep Learning
  ----------------------- ----------------------- -----------------------
  Feature engineering     Often required          Often learned
                                                  automatically

  Data requirement        Usually lower           Usually higher

  Model structure         Many algorithm families Neural networks

  Representation          Often manually designed Learned hierarchically

  Typical strengths       Tabular/structured data Images, audio, text and
                                                  other high-dimensional
                                                  data
  -----------------------------------------------------------------------

Deep Learning is especially useful for complex perception and
representation-learning problems such as image and speech recognition.

------------------------------------------------------------------------

# 2. Neural Network Fundamentals

A neural network is composed of interconnected computational units
called **neurons**.

A basic neuron computes:

$$
z = w^Tx + b
$$

and then applies an activation function:

$$
a = f(z)
$$

Where:

-   $x$ = input vector
-   $w$ = weight vector
-   $b$ = bias
-   $z$ = pre-activation
-   $f$ = activation function
-   $a$ = neuron output

------------------------------------------------------------------------

## 3. Perceptron

The **Perceptron** is one of the simplest neural-network algorithms.

It:

1.  Receives inputs.
2.  Computes a weighted sum.
3.  Applies an activation function.
4.  Produces an output.

### Perceptron equation

$$
z = \sum_{i=1}^{n} w_i x_i + b
$$

For a classic binary perceptron:

$$
\hat{y} =
\begin{cases}
1 & z \ge 0 \\
0 & z < 0
\end{cases}
$$

### Limitation

A single perceptron can solve only **linearly separable** classification
problems.

This limitation motivates multi-layer neural networks.

------------------------------------------------------------------------

# 4. Multi-Layer Perceptron (MLP)

An **MLP** contains:

-   Input layer
-   One or more hidden layers
-   Output layer

Each connection has a weight, and neurons apply activation functions to
their weighted inputs.

A network becomes **deep** when it contains multiple computational
layers.

### Basic flow

``` text
Input
  ↓
Hidden Layer 1
  ↓
Hidden Layer 2
  ↓
...
  ↓
Output
```

MLPs are commonly used for:

-   Classification
-   Regression
-   Tabular data
-   Representation learning

------------------------------------------------------------------------

# 5. Forward Propagation

**Forward propagation** is the process of passing input data through the
network to produce a prediction.

For one layer:

$$
z^{[l]} = W^{[l]}a^{[l-1]} + b^{[l]}
$$

$$
a^{[l]} = f(z^{[l]})
$$

For the first layer:

$$
a^{[0]} = x
$$

The final activation is used to generate the model prediction.

### Forward-pass pipeline

``` text
Input
 ↓
Linear transformation
 ↓
Activation
 ↓
Linear transformation
 ↓
Activation
 ↓
Prediction
```

------------------------------------------------------------------------

# 6. Activation Functions

Activation functions introduce **non-linearity** into neural networks.

Without nonlinear activations, stacking linear layers would still
produce an overall linear transformation.

## 6.1 Sigmoid

$$
\sigma(x)=\frac{1}{1+e^{-x}}
$$

Range:

$$
0 < \sigma(x) < 1
$$

Common use:

-   Binary classification output

Limitation:

-   Can suffer from vanishing gradients.

------------------------------------------------------------------------

## 6.2 Tanh

$$
\tanh(x)
$$

Range:

$$
-1 < \tanh(x) < 1
$$

It is zero-centered but can also suffer from vanishing gradients.

------------------------------------------------------------------------

## 6.3 ReLU

$$
ReLU(x)=\max(0,x)
$$

Advantages:

-   Simple
-   Computationally efficient
-   Helps reduce vanishing-gradient problems compared with sigmoid/tanh
    in many settings

Limitation:

-   Can produce inactive/"dead" neurons for consistently negative
    inputs.

------------------------------------------------------------------------

## 6.4 Softmax

For class $i$:

$$
softmax(z_i)=\frac{e^{z_i}}{\sum_j e^{z_j}}
$$

It converts logits into a probability distribution whose values sum to
1.

Common use:

-   Multi-class classification output layer

------------------------------------------------------------------------

# 7. Loss Functions

A **loss function** measures the difference between a model prediction
and the target.

Training attempts to minimize the loss.

## Common losses

### Mean Squared Error

For regression:

$$
MSE=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

### Binary Cross-Entropy

For binary classification:

$$
L=-[y\log(\hat{y})+(1-y)\log(1-\hat{y})]
$$

### Categorical Cross-Entropy

For multi-class classification:

$$
L=-\sum_i y_i\log(\hat{y}_i)
$$

### Hinge Loss

A margin-based loss commonly associated with binary classification:

$$
L=\max(0,1-y\hat{y})
$$

------------------------------------------------------------------------

# 8. Cost Function vs Loss Function

-   **Loss:** Error for one training example.
-   **Cost:** Aggregate loss over a dataset, commonly an average.

A simplified view:

``` text
Individual example → Loss
Entire batch/dataset → Cost / average loss
```

Terminology can vary between sources, so always check the specific
formulation being used.

------------------------------------------------------------------------

# 9. Gradient Descent

Neural networks learn by adjusting parameters to reduce the loss.

Basic update:

$$
\theta := \theta - \eta\nabla_\theta L
$$

Where:

-   $\theta$ = model parameters
-   $\eta$ = learning rate
-   $\nabla_\theta L$ = gradient of loss with respect to parameters

### Intuition

``` text
Calculate prediction
      ↓
Calculate loss
      ↓
Calculate gradients
      ↓
Update weights
      ↓
Repeat
```

------------------------------------------------------------------------

# 10. Batch, Stochastic and Mini-Batch Gradient Descent

### Batch Gradient Descent

Uses the entire training dataset for one parameter update.

### Stochastic Gradient Descent (SGD)

Uses one training example per update.

### Mini-Batch Gradient Descent

Uses a small batch of examples per update.

Mini-batch training is widely used in practical deep learning because it
provides a useful balance between computational efficiency and update
frequency.

------------------------------------------------------------------------

# 11. Backpropagation

**Backpropagation** calculates how much each model parameter contributed
to the final loss.

It uses the **chain rule** to propagate gradients backward through the
network.

### Conceptual process

``` text
Forward pass
     ↓
Prediction
     ↓
Loss calculation
     ↓
Backward pass
     ↓
Gradients
     ↓
Parameter update
```

For a parameter $\theta$:

$$
\theta := \theta - \eta\frac{\partial L}{\partial\theta}
$$

### Why it matters

Backpropagation makes it practical to train networks containing many
layers and parameters.

------------------------------------------------------------------------

# 12. Optimizers

An optimizer determines how model parameters are updated using
gradients.

## SGD

Basic gradient-based update:

$$
\theta_{t+1}=\theta_t-\eta g_t
$$

## Momentum

Uses a moving direction based on previous gradients to accelerate
learning and reduce oscillations.

## RMSProp

Adapts the learning rate using a moving average of squared gradients.

## Adam

Adam combines ideas from momentum and adaptive learning rates.

It is widely used as a practical starting optimizer for neural-network
training.

### Practical rule

Do not choose an optimizer only because it is popular. Monitor:

-   Training loss
-   Validation loss
-   Learning rate
-   Convergence
-   Generalization

------------------------------------------------------------------------

# 13. Vanishing and Exploding Gradients

During backpropagation, gradients can become:

-   Extremely small → **vanishing gradients**
-   Extremely large → **exploding gradients**

### Effects

Vanishing gradients can make early layers learn very slowly.

Exploding gradients can cause unstable training or numerical problems.

### Common mitigation techniques

-   Appropriate activation functions
-   Proper initialization
-   Batch normalization
-   Residual connections
-   Gradient clipping
-   Suitable optimizers
-   Careful learning-rate selection

------------------------------------------------------------------------

# 14. Weight Initialization

Initialization affects whether training starts in a useful region.

Common approaches include:

-   Zero initialization for biases
-   Xavier/Glorot initialization
-   He initialization

For ReLU-family activations, He initialization is commonly used.

Poor initialization can contribute to unstable or slow training.

------------------------------------------------------------------------

# 15. Regularization

Deep networks can overfit training data.

Regularization helps improve generalization.

## L1 Regularization

Adds:

$$
\lambda\sum_i |w_i|
$$

## L2 Regularization

Adds:

$$
\lambda\sum_i w_i^2
$$

In modern deep learning, weight decay is commonly used as a practical
form of parameter regularization.

------------------------------------------------------------------------

# 16. Dropout

**Dropout** randomly disables a subset of activations during training.

Example:

``` text
Before dropout:
● ● ● ● ● ●

After dropout:
● ○ ● ○ ● ●
```

Benefits:

-   Reduces reliance on individual neurons
-   Can reduce overfitting

Dropout is normally active during training and disabled during
evaluation.

------------------------------------------------------------------------

# 17. Batch Normalization

Batch normalization normalizes intermediate activations using statistics
computed from a mini-batch during training.

General form:

$$
\hat{x}=\frac{x-\mu_B}{\sqrt{\sigma_B^2+\epsilon}}
$$

Then learnable parameters scale and shift the normalized value:

$$
y=\gamma\hat{x}+\beta
$$

Potential benefits:

-   More stable optimization
-   Allows useful learning rates
-   Can improve training behavior

------------------------------------------------------------------------

# 18. Hyperparameters

Hyperparameters are values chosen before or around training rather than
directly learned as model parameters.

Important examples:

-   Learning rate
-   Batch size
-   Number of epochs
-   Number of layers
-   Number of neurons
-   Dropout rate
-   Weight decay
-   Optimizer
-   Activation function

### Practical tuning order

1.  Learning rate
2.  Batch size
3.  Model capacity
4.  Regularization
5.  Optimizer settings
6.  Architecture-specific parameters

Always tune using validation data rather than the test set.

------------------------------------------------------------------------

# 19. Training, Validation and Test Sets

A standard workflow:

``` text
Dataset
   │
   ├── Training set → learn parameters
   │
   ├── Validation set → tune choices
   │
   └── Test set → final evaluation
```

The test set should remain isolated until final evaluation.

------------------------------------------------------------------------

# 20. Underfitting vs Overfitting

### Underfitting

Model performs poorly on both training and validation data.

Possible causes:

-   Model too simple
-   Insufficient training
-   Excessive regularization

### Overfitting

Model performs well on training data but poorly on unseen data.

Possible causes:

-   Excessive model capacity
-   Limited data
-   Weak regularization
-   Training for too long

------------------------------------------------------------------------

# 21. Artificial Neural Networks (ANN)

ANNs are general-purpose neural networks built from connected neurons.

For tabular problems, an MLP is a common ANN architecture.

Typical structure:

``` text
Features
   ↓
Dense Layer
   ↓
Activation
   ↓
Dense Layer
   ↓
Activation
   ↓
Output Layer
```

Example applications:

-   Classification
-   Regression
-   Customer churn prediction
-   Risk prediction

------------------------------------------------------------------------

# 22. Convolutional Neural Networks (CNNs)

CNNs are designed to work effectively with grid-like data such as
images.

Core concepts:

-   Convolution
-   Filters/kernels
-   Feature maps
-   Stride
-   Padding
-   Pooling

### Basic CNN pipeline

``` text
Image
 ↓
Convolution
 ↓
Activation
 ↓
Pooling
 ↓
Convolution
 ↓
Activation
 ↓
Pooling
 ↓
Flatten / Global Pooling
 ↓
Fully Connected Layer
 ↓
Prediction
```

CNNs learn local spatial patterns and can build hierarchical visual
representations.

------------------------------------------------------------------------

# 23. Transfer Learning

**Transfer learning** starts with a model trained on one task/dataset
and adapts it to another related task.

Typical workflow:

``` text
Pretrained model
      ↓
Replace/adapt final layer
      ↓
Train on target dataset
      ↓
Optional fine-tuning
```

Benefits:

-   Requires less target-domain data
-   Reduces training cost
-   Often improves performance

Relevant architectures include:

-   ResNet
-   DenseNet
-   EfficientNet

------------------------------------------------------------------------

# 24. Data Augmentation

Data augmentation creates modified versions of training examples.

For images:

-   Rotation
-   Cropping
-   Flipping
-   Translation
-   Scaling
-   Color transformations

The goal is to increase variation in the training data and improve
generalization.

Augmentation must preserve the semantic meaning of the target label.

------------------------------------------------------------------------

# 25. Object Detection

Object detection identifies:

1.  **What** objects are present.
2.  **Where** they are located.

Common concepts:

-   Bounding boxes
-   Classification
-   Localization
-   Intersection over Union (IoU)

Examples of object-detection families include:

-   YOLO
-   SSD

------------------------------------------------------------------------

# 26. Recurrent Neural Networks (RNNs)

RNNs process sequential data by maintaining information from previous
time steps.

Conceptually:

$$
h_t=f(W_xx_t+W_hh_{t-1}+b)
$$

Where:

-   $x_t$ = current input
-   $h_{t-1}$ = previous hidden state
-   $h_t$ = current hidden state

Applications:

-   Sequence modeling
-   Time-series data
-   Language tasks

### Main limitation

RNNs can suffer from vanishing/exploding gradients and difficulty
learning long-term dependencies.

------------------------------------------------------------------------

# 27. LSTM

**Long Short-Term Memory (LSTM)** networks were designed to handle
long-term dependencies better than basic RNNs.

LSTMs use gates to control information flow:

-   Forget gate
-   Input gate
-   Output gate

Conceptually:

``` text
Previous state ──┐
                 ↓
Input ───────→ LSTM Cell ───→ New state
```

------------------------------------------------------------------------

# 28. GRU

**Gated Recurrent Unit (GRU)** is another gated recurrent architecture.

Compared with LSTM, GRU uses a simpler gating structure.

Main gates:

-   Update gate
-   Reset gate

GRUs can provide useful sequence modeling with fewer components than
LSTMs.

------------------------------------------------------------------------

# 29. Attention Mechanism

Attention allows a model to assign different importance to different
parts of an input sequence while producing an output.

Instead of treating every input element equally, the model learns where
to focus.

A simplified attention formulation:

$$
Attention(Q,K,V)=softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

Where:

-   $Q$ = queries
-   $K$ = keys
-   $V$ = values
-   $d_k$ = key dimensionality

Attention became a fundamental building block for modern Transformer
architectures.

------------------------------------------------------------------------

# 30. Transformers

Transformers use attention-based architecture instead of recurrence as
the central sequence-processing mechanism.

Important components:

-   Tokenization
-   Embeddings
-   Positional information
-   Self-attention
-   Multi-head attention
-   Feed-forward networks
-   Residual connections
-   Layer normalization

### High-level structure

``` text
Tokens
  ↓
Embeddings
  ↓
Positional information
  ↓
Self-Attention
  ↓
Feed-Forward Network
  ↓
Repeated Transformer Blocks
  ↓
Output
```

Transformers are foundational to modern NLP and LLM systems.

------------------------------------------------------------------------

# 31. NLP Foundations

Important Deep Learning NLP concepts include:

### Tokenization

Converts text into tokens.

Examples:

-   Byte Pair Encoding (BPE)
-   WordPiece

### Embeddings

Represent tokens as dense vectors.

Examples:

-   Word2Vec
-   GloVe

### Sequence models

-   RNN
-   LSTM
-   GRU
-   Attention
-   Transformers

------------------------------------------------------------------------

# 32. BERT and GPT

### BERT

BERT is a Transformer-based language model designed primarily around
bidirectional contextual representation learning.

Typical uses:

-   Text classification
-   Question answering
-   Named entity recognition
-   Sentence representation

### GPT

GPT-style architectures use Transformer decoder blocks and are designed
for autoregressive language modeling.

A simplified objective is to predict the next token:

$$
P(x_t|x_1,\dots,x_{t-1})
$$

------------------------------------------------------------------------

# 33. Large Language Models (LLMs)

LLMs are large neural language models trained on very large text
corpora.

A typical lifecycle can include:

``` text
Data collection
      ↓
Cleaning / filtering
      ↓
Tokenization
      ↓
Pretraining
      ↓
Instruction tuning / fine-tuning
      ↓
Evaluation
      ↓
Deployment
      ↓
Monitoring
```

For an AI/ML Engineer, important areas include:

-   Transformer architecture
-   Training pipelines
-   Fine-tuning
-   Evaluation
-   Inference
-   Quantization
-   Deployment
-   Monitoring

------------------------------------------------------------------------

# 34. Autoencoders

An autoencoder learns to reconstruct its input.

Architecture:

``` text
Input
  ↓
Encoder
  ↓
Latent representation
  ↓
Decoder
  ↓
Reconstructed input
```

Main components:

-   Encoder
-   Latent representation
-   Decoder

Applications include:

-   Representation learning
-   Dimensionality reduction
-   Anomaly detection
-   Denoising

------------------------------------------------------------------------

# 35. Variational Autoencoders (VAE)

VAEs learn a probabilistic latent representation rather than simply
mapping an input to one deterministic latent vector.

They combine:

-   Reconstruction objective
-   Latent-space regularization

A VAE is a foundational generative-model architecture.

------------------------------------------------------------------------

# 36. Generative Adversarial Networks (GANs)

GANs contain two competing networks:

### Generator

Creates synthetic samples.

### Discriminator

Attempts to distinguish real samples from generated samples.

``` text
Random Noise
     ↓
 Generator
     ↓
Fake Data ───────┐
                 ↓
             Discriminator
                 ↑
Real Data ───────┘
```

Training is formulated as a competition between the generator and
discriminator.

Examples include:

-   DCGAN
-   StyleGAN

------------------------------------------------------------------------

# 37. Diffusion Models

Diffusion models generate data by learning a reverse denoising process.

High-level idea:

``` text
Clean data
   ↓
Add noise repeatedly
   ↓
Highly noisy representation
   ↓
Learn reverse denoising
   ↓
Generated sample
```

They form the basis of modern image-generation systems such as Stable
Diffusion.

------------------------------------------------------------------------

# 38. Deep Learning Training Pipeline

A practical training workflow:

``` text
1. Define problem
       ↓
2. Collect dataset
       ↓
3. Explore data
       ↓
4. Clean / preprocess
       ↓
5. Split train / validation / test
       ↓
6. Build baseline
       ↓
7. Define neural network
       ↓
8. Choose loss + optimizer
       ↓
9. Train
       ↓
10. Validate
       ↓
11. Tune hyperparameters
       ↓
12. Test
       ↓
13. Save model
       ↓
14. Deploy
       ↓
15. Monitor
```

------------------------------------------------------------------------

# 39. PyTorch

For this learning path, **PyTorch** is the preferred Deep Learning
framework.

Core concepts to learn:

-   `torch.Tensor`
-   `Dataset`
-   `DataLoader`
-   `nn.Module`
-   Layers
-   Loss functions
-   Optimizers
-   Autograd
-   Training loops
-   Evaluation loops
-   Model serialization
-   GPU/CPU device management

### Typical PyTorch workflow

``` python
model = Model()
criterion = LossFunction()
optimizer = Optimizer(model.parameters())

for epoch in range(epochs):

    model.train()

    for X, y in train_loader:
        optimizer.zero_grad()

        predictions = model(X)
        loss = criterion(predictions, y)

        loss.backward()
        optimizer.step()
```

Evaluation:

``` python
model.eval()

with torch.no_grad():
    predictions = model(X)
```

------------------------------------------------------------------------

# 40. CPU vs GPU

Deep Learning often involves large matrix and tensor operations.

GPUs can accelerate these workloads because they are designed for highly
parallel computation.

Typical workflow:

``` python
device = "cuda" if torch.cuda.is_available() else "cpu"

model = model.to(device)
X = X.to(device)
y = y.to(device)
```

For resource-constrained hardware, start with small models and datasets
and use cloud GPU resources when necessary.

------------------------------------------------------------------------

# 41. Model Evaluation

Choose metrics according to the problem.

### Classification

-   Accuracy
-   Precision
-   Recall
-   F1-score
-   ROC-AUC
-   Confusion matrix

### Regression

-   MAE
-   MSE
-   RMSE
-   $R^2$

Do not rely on accuracy alone when classes are imbalanced.

------------------------------------------------------------------------

# 42. Common Deep Learning Failure Modes

### Overfitting

Training performance improves while validation performance worsens.

Possible responses:

-   More data
-   Data augmentation
-   Dropout
-   Weight decay
-   Early stopping
-   Smaller model

### Underfitting

Both training and validation performance are poor.

Possible responses:

-   Increase model capacity
-   Train longer
-   Reduce excessive regularization
-   Improve features/data representation

### Unstable training

Possible causes:

-   Learning rate too high
-   Poor initialization
-   Exploding gradients
-   Bad preprocessing

------------------------------------------------------------------------

# 43. Deep Learning Interview Checklist

Before moving to advanced AI, be able to explain:

-   What Deep Learning is
-   ML vs DL
-   Perceptron
-   MLP
-   Forward propagation
-   Backpropagation
-   Chain rule
-   Activation functions
-   Loss functions
-   Gradient descent
-   SGD vs batch vs mini-batch
-   Adam
-   Learning rate
-   Vanishing/exploding gradients
-   Weight initialization
-   Regularization
-   Dropout
-   Batch normalization
-   CNN
-   Convolution
-   Pooling
-   Transfer learning
-   Data augmentation
-   RNN
-   LSTM
-   GRU
-   Attention
-   Transformer
-   BERT
-   GPT
-   Autoencoder
-   VAE
-   GAN
-   Diffusion models
-   Training/validation/test split
-   Overfitting and underfitting
-   PyTorch training loop

------------------------------------------------------------------------

# 44. Recommended Learning Order

Follow this order rather than jumping directly into LLMs:

``` text
Deep Learning Basics
        ↓
Perceptron
        ↓
MLP / ANN
        ↓
Forward Propagation
        ↓
Loss Functions
        ↓
Gradient Descent
        ↓
Backpropagation
        ↓
Optimizers
        ↓
Regularization
        ↓
Batch Normalization + Dropout
        ↓
PyTorch
        ↓
CNN
        ↓
Transfer Learning
        ↓
RNN
        ↓
LSTM / GRU
        ↓
Attention
        ↓
Transformers
        ↓
BERT / GPT
        ↓
LLMs
        ↓
Generative Models
        ↓
MLOps + Deployment
```

------------------------------------------------------------------------

# 45. AI/ML Engineering Focus

For an ML Engineer, Deep Learning should not stop at theory.

The practical progression is:

``` text
Theory
  ↓
Mathematical intuition
  ↓
PyTorch implementation
  ↓
Experiments
  ↓
Model evaluation
  ↓
Experiment tracking
  ↓
Model optimization
  ↓
Deployment
  ↓
Monitoring
```

The uploaded roadmap places Deep Learning after Core ML and before
advanced CV/NLP, LLMs, MLOps, projects and interview preparation. It
specifically identifies tensors, forward propagation, backpropagation,
activations, optimizers, vanishing/exploding gradients, loss functions,
perceptrons, MLPs, batch normalization and dropout as foundational
topics. fileciteturn1file1L1-L8

The 100 Days of Deep Learning source follows the same progression from
Deep Learning fundamentals and neural-network types into perceptrons,
MLPs, forward propagation, loss functions, backpropagation and
optimization, then later attention, RNN/LSTM and Transformer-related
topics. fileciteturn1file0L25-L40 fileciteturn1file8L1-L12

------------------------------------------------------------------------

## 46. Final Mental Model

Remember the complete training loop:

$$
\boxed{
Input
\rightarrow
Forward\ Pass
\rightarrow
Prediction
\rightarrow
Loss
\rightarrow
Backpropagation
\rightarrow
Gradients
\rightarrow
Optimizer
\rightarrow
Updated\ Parameters
}
$$

Repeat this process over many batches and epochs until the model learns
useful representations that generalize to unseen data.

------------------------------------------------------------------------

## Sources

-   CampusX --- **100 Days of Deep Learning** course material
-   AI/ML roadmap --- **Zero to Advanced: ML → DL → Transformers → LLMs
    → MLOps → Projects → Interview Prep**
