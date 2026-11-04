# Early Stopping & Hyperparameter Tuning with TensorFlow/Keras

## 1. Early Stopping

**Early stopping** is a regularization technique that stops training
when performance on a validation metric stops improving. It can reduce
overfitting and unnecessary training.

### How it works

``` text
Train for one epoch
       ↓
Check validation metric
       ↓
Improvement?
  Yes → Save best state; reset patience
  No  → Increase wait counter
       ↓
Wait counter reaches patience?
  No → Continue
  Yes → Stop training
```

### Important parameters

  Parameter                Meaning
  ------------------------ -----------------------------------------
  `monitor`                Metric to watch, e.g. `val_loss`
  `patience`               Epochs to wait without improvement
  `min_delta`              Minimum change counted as improvement
  `mode`                   `min` or `max`
  `restore_best_weights`   Restore weights from best epoch
  `start_from_epoch`       Ignore initial epochs before monitoring

### Basic Keras example

``` python
import tensorflow as tf
from tensorflow import keras

early_stopping = keras.callbacks.EarlyStopping(
    monitor="val_loss",
    patience=5,
    min_delta=0.001,
    mode="min",
    restore_best_weights=True
)

history = model.fit(
    X_train,
    y_train,
    validation_data=(X_val, y_val),
    epochs=100,
    batch_size=32,
    callbacks=[early_stopping]
)
```

`val_loss` is minimized. If it does not improve by at least `min_delta`
for 5 consecutive epochs, training stops. The best weights are restored.
The test set must not be used for early stopping.

## 2. ModelCheckpoint

`ModelCheckpoint` saves the best model/checkpoint to disk. It
complements early stopping.

``` python
checkpoint = keras.callbacks.ModelCheckpoint(
    filepath="best_model.keras",
    monitor="val_loss",
    mode="min",
    save_best_only=True
)

callbacks = [
    keras.callbacks.EarlyStopping(
        monitor="val_loss",
        patience=5,
        restore_best_weights=True
    ),
    checkpoint
]

history = model.fit(
    X_train,
    y_train,
    validation_data=(X_val, y_val),
    epochs=100,
    callbacks=callbacks
)
```

-   `EarlyStopping`: decides when to stop and can restore the best
    in-memory weights.
-   `ModelCheckpoint`: saves the best model/checkpoint to disk.

## 3. Hyperparameters and Hyperparameter Tuning

**Hyperparameters** are configuration values chosen outside the model's
weight-learning process.

  -----------------------------------------------------------------------
  Model parameters                    Hyperparameters
  ----------------------------------- -----------------------------------
  Learned during training             Set or selected before/during
                                      experiments

  Weights and biases                  Learning rate, batch size, layer
                                      count, dropout rate
  -----------------------------------------------------------------------

**Hyperparameter tuning** searches for configurations that perform well
on validation data.

Examples of tunable hyperparameters: - Learning rate: `1e-2`, `1e-3`,
`1e-4` - Hidden layers: `1`, `2`, `3` - Units per layer: `32`, `64`,
`128` - Batch size: `16`, `32`, `64` - Dropout: `0.2`, `0.3`, `0.5` -
Optimizer: Adam, RMSprop, SGD

## 4. Common Tuning Strategies

  -----------------------------------------------------------------------
  Strategy                How it works            Limitation / strength
  ----------------------- ----------------------- -----------------------
  Manual search           Choose values and run   Simple, but can be slow
                          experiments             

  Grid search             Test every specified    Expensive for large
                          combination             search spaces

  Random search           Sample configurations   Broad exploration; best
                          randomly                configuration is not
                                                  guaranteed

  Bayesian optimization   Use previous trial      More complex, can
                          results to guide future reduce wasted trials
                          trials                  

  Hyperband               Allocate more resources Useful when training is
                          to promising trials and expensive
                          stop weaker ones        
  -----------------------------------------------------------------------

## 5. KerasTuner

KerasTuner provides search algorithms for Keras models, including
`RandomSearch`, `GridSearch`, `BayesianOptimization`, and `Hyperband`.

Install:

``` bash
pip install keras-tuner
```

Imports:

``` python
import keras_tuner as kt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
```

## 6. Build a Tunable Model

The model-building function receives a `HyperParameters` object. This
example is for binary classification. Define `input_dim` as the number
of input features.

``` python
def build_model(hp):
    model = keras.Sequential()
    model.add(keras.Input(shape=(input_dim,)))

    num_layers = hp.Int("num_layers", min_value=1, max_value=3)

    for i in range(num_layers):
        units = hp.Choice(
            f"units_{i}",
            values=[32, 64, 128]
        )
        model.add(layers.Dense(units, activation="relu"))

        dropout_rate = hp.Float(
            f"dropout_{i}",
            min_value=0.0,
            max_value=0.5,
            step=0.1
        )
        if dropout_rate > 0:
            model.add(layers.Dropout(dropout_rate))

    model.add(layers.Dense(1, activation="sigmoid"))

    learning_rate = hp.Choice(
        "learning_rate",
        values=[1e-2, 1e-3, 1e-4]
    )

    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )
    return model
```

For multiclass classification or regression, change the output layer,
loss, and metrics to match the task.

## 7. Random Search

``` python
tuner = kt.RandomSearch(
    hypermodel=build_model,
    objective="val_accuracy",
    max_trials=10,
    executions_per_trial=1,
    directory="tuning_results",
    project_name="mlp_random_search",
    overwrite=True
)

early_stopping = keras.callbacks.EarlyStopping(
    monitor="val_loss",
    patience=5,
    restore_best_weights=True
)

tuner.search(
    X_train,
    y_train,
    validation_data=(X_val, y_val),
    epochs=50,
    batch_size=32,
    callbacks=[early_stopping]
)
```

Key arguments: - `objective`: validation metric to optimize. -
`max_trials`: maximum number of configurations to try. -
`executions_per_trial`: model executions per configuration. -
`directory` and `project_name`: where experiment results are stored.

The tuner compares trials using `val_accuracy`; early stopping monitors
`val_loss` within each trial. These are different metrics serving
different purposes.

## 8. Retrieve the Best Hyperparameters and Model

``` python
best_hp = tuner.get_best_hyperparameters(num_trials=1)[0]

print("Layers:", best_hp.get("num_layers"))
print("Learning rate:", best_hp.get("learning_rate"))

for i in range(best_hp.get("num_layers")):
    print(f"Layer {i + 1} units:", best_hp.get(f"units_{i}"))

best_model = tuner.get_best_models(num_models=1)[0]
```

Evaluate only after tuning is complete:

``` python
test_loss, test_accuracy = best_model.evaluate(X_test, y_test)
print("Test accuracy:", test_accuracy)
```

## 9. Hyperband

Hyperband allocates training resources adaptively. Weaker trials are
stopped, while promising trials receive more resources.

``` python
tuner = kt.Hyperband(
    hypermodel=build_model,
    objective="val_accuracy",
    max_epochs=50,
    factor=3,
    hyperband_iterations=1,
    directory="tuning_results",
    project_name="mlp_hyperband",
    overwrite=True
)

tuner.search(
    X_train,
    y_train,
    validation_data=(X_val, y_val),
    epochs=50,
    callbacks=[
        keras.callbacks.EarlyStopping(
            monitor="val_loss",
            patience=5,
            restore_best_weights=True
        )
    ]
)
```

-   `max_epochs`: maximum epoch budget for a trial.
-   `factor`: controls how aggressively lower-performing trials are
    eliminated.
-   `hyperband_iterations`: number of Hyperband runs.

Hyperband allocates resources across trials. `EarlyStopping` monitors an
individual trial's validation metric. They can be used together.

## 10. Train the Selected Model

After tuning, rebuild the selected configuration and train it. Keep the
test set out of model selection.

``` python
best_hp = tuner.get_best_hyperparameters(num_trials=1)[0]
final_model = tuner.hypermodel.build(best_hp)

callbacks = [
    keras.callbacks.EarlyStopping(
        monitor="val_loss",
        patience=7,
        restore_best_weights=True
    ),
    keras.callbacks.ModelCheckpoint(
        "best_final_model.keras",
        monitor="val_loss",
        save_best_only=True
    )
]

history = final_model.fit(
    X_train,
    y_train,
    validation_data=(X_val, y_val),
    epochs=100,
    batch_size=32,
    callbacks=callbacks
)
```

The validation set guides tuning and early stopping, so it is not an
unbiased final performance estimate. Evaluate the selected model on the
held-out test set after all decisions are complete.

## 11. Best Practices

1.  Split data into training, validation, and test sets before model
    development.
2.  Prevent data leakage: fit preprocessing (scaling, imputation, etc.)
    on training data only.
3.  Select an objective that matches the task: `val_loss`, F1, PR-AUC,
    or another relevant metric.
4.  Use early stopping to avoid unnecessary epochs.
5.  Keep the test set untouched during tuning.
6.  Start with a small search space and tune influential hyperparameters
    first.
7.  Record configurations, metrics, and random seeds.
8.  For imbalanced classification, do not rely on accuracy alone;
    consider precision, recall, F1, PR-AUC, or ROC-AUC.
9.  Re-evaluate the final selected model on the held-out test set.

## 12. Early Stopping vs Hyperparameter Tuning

  -----------------------------------------------------------------------
  Early Stopping                      Hyperparameter Tuning
  ----------------------------------- -----------------------------------
  Decides when one training run       Searches for good model/training
  should stop                         configurations

  Monitors validation performance     Compares validation performance
  over epochs                         across trials

  Uses callbacks such as              Uses random search, Bayesian
  `EarlyStopping`                     optimization, Hyperband, etc.

  Can reduce overfitting and wasted   Helps select learning rate,
  epochs                              architecture, batch size, etc.
  -----------------------------------------------------------------------

## 13. Interview Questions

**1. What is early stopping?**\
A regularization technique that stops training when a monitored
validation metric no longer improves sufficiently.

**2. What does `patience` mean?**\
The number of epochs without sufficient improvement allowed before
stopping.

**3. Why use `restore_best_weights=True`?**\
It restores weights from the epoch with the best monitored metric.

**4. What is hyperparameter tuning?**\
Searching for suitable configuration values such as learning rate, batch
size, and architecture.

**5. Grid search vs random search?**\
Grid search tests every specified combination; random search samples
combinations.

**6. What is Bayesian optimization?**\
A method that uses previous trial results to guide the selection of
future configurations.

**7. What is Hyperband?**\
A tuning strategy that allocates more training resources to promising
configurations and stops weaker trials early.

**8. Why must the test set not be used for tuning?**\
Repeatedly selecting models based on test performance leaks test
information into development and makes the final estimate unreliable.

**9. Does early stopping replace hyperparameter tuning?**\
No. Early stopping selects a stopping point; tuning searches for good
hyperparameter configurations.

**10. Can EarlyStopping and ModelCheckpoint be used together?**\
Yes. One controls stopping and optional in-memory weight restoration;
the other saves the best model/checkpoint to disk.

## 14. Final Mental Model

``` text
Define model and search space
          ↓
Select a tuning strategy
          ↓
Build a candidate model
          ↓
Train on training data
          ↓
Monitor validation performance
          ↓
EarlyStopping may stop this trial
          ↓
Tuner compares trial results
          ↓
Select best hyperparameters
          ↓
Train selected model
          ↓
Evaluate on held-out test data
```

**Remember:** - **Early Stopping:** When should training stop? -
**Hyperparameter Tuning:** Which configuration should be used? -
**ModelCheckpoint:** Which model state should be saved? - **Validation
Set:** Which choices guide model development? - **Test Set:** How well
does the final selected model generalize?
