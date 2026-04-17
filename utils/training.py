def train_model(model, X_train, y_train, X_val=None, y_val=None, epochs=50, batch_size=32):

    """Train a Keras model with optional validation data."""

    if X_val is not None and y_val is not None:

        history = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=epochs, batch_size=batch_size)

    else:

        history = model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)
        
    return history
