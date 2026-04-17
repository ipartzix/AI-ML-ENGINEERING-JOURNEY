import tensorflow as tf

from tensorflow.keras.layers import Dense, Dropout

from tensorflow.keras.models import Sequential


def build_mlp(input_dim, layers=[64, 32], activation='relu', output_dim=1, output_activation='sigmoid'):
    """Build a simple feedforward MLP model."""
    
    model = Sequential()
    for i, units in enumerate(layers):
        if i == 0:
            model.add(Dense(units, activation=activation, input_dim=input_dim))
        else:
            model.add(Dense(units, activation=activation))
        model.add(Dropout(0.2))
    model.add(Dense(output_dim, activation=output_activation))
    return model


def compile_model(model, loss='binary_crossentropy', optimizer='adam', metrics=['accuracy']):
    """Compile a Keras model."""
    model.compile(loss=loss, optimizer=optimizer, metrics=metrics)
    return model
