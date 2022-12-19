# Import necessary libraries
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import NeuralNetForm

# Load the dataset
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

# Preprocess the data
X_train = X_train.reshape(-1, 28 * 28) / 255.
X_test = X_test.reshape(-1, 28 * 28) / 255.

def index(request):
    # Handle user input for number of layers and nodes
    if request.method == 'POST':
        form = NeuralNetForm(request.POST)
        if form.is_valid():
            # Build the neural network model
            model = Sequential()
            for i in range(form.cleaned_data['layers']):
                model.add(Dense(units=form.cleaned_data['nodes'], activation='relu', input_dim=28*28))
            model.add(Dense(units=10, activation='softmax'


# Load the data from UCI breast cancer classification dataset
data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data", header=None)

# Preprocess the data by extracting the features and labels
X = data.iloc[:, 2:].values
y = data.iloc[:, 1].values

# Convert the labels from string to numeric
y = np.where(y == "M", 1, 0)

# Scale the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Build the neural network model
model = Sequential()
model.add(Dense(units=16, activation='relu', input_dim=30))
model.add(Dense(units=8, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X_train_std, y_train, epochs=100, batch_size=16)

# Evaluate the model
test_loss, test_acc = model.evaluate(X_test_std, y_test)
print(test_acc)

# Build the random forest model
model = RandomForestClassifier(n_estimators=100, criterion='gini', random_state=1)

# Train the model
model.fit(X_train_std, y_train)

# Evaluate the model
print(model.score(X_test_std, y_test))

# Build the random forest model
model = RandomForestClassifier(n_estimators=100, criterion='gini', random_state=1)

# Train the model
model.fit(X_train_std, y_train)

# Evaluate the model
print(model.score(X_test_std, y_test))
