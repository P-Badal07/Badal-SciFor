# -*- coding: utf-8 -*-
"""machine_learning.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Lq5w_uKZDrvCUO1okgz_c0ICsHBLuerW
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = load_iris()
X, y = data['data'], data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Shape of X_train (training features):", X_train.shape)
print("Shape of y_train (training labels):", y_train.shape)
print("Shape of X_test (testing features):", X_test.shape)
print("Shape of y_test (testing labels):", y_test.shape)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Example of scaled training features:")
print(X_train_scaled[0])

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

model_tf = Sequential([
    Dense(64, activation='relu', input_shape=(4,)),
    Dense(64, activation='relu'),
    Dense(3, activation='softmax')
])

print("Summary of TensorFlow model:")
model_tf.summary()

model_tf.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model_tf.fit(X_train_scaled, y_train, epochs=50, verbose=0)

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

class NeuralNet(nn.Module):
    def __init__(self):
        super(NeuralNet, self).__init__()
        self.fc1 = nn.Linear(4, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 3)
        self.relu = nn.ReLU()
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)
        return self.softmax(x)

model_pt = NeuralNet()

print("PyTorch model architecture:")
print(model_pt)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model_pt.parameters(), lr=0.001)

X_train_pt = torch.tensor(X_train_scaled, dtype=torch.float32)
y_train_pt = torch.tensor(y_train, dtype=torch.long)
train_dataset = TensorDataset(X_train_pt, y_train_pt)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

for epoch in range(50):
    running_loss = 0.0
    for inputs, labels in train_loader:
        optimizer.zero_grad()
        outputs = model_pt(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

print(f"Epoch {epoch + 1}, Loss: {running_loss / len(train_loader)}")

import numpy as np
from sklearn.metrics import accuracy_score

y_pred_tf = np.argmax(model_tf.predict(X_test_scaled), axis=1)
accuracy_tf = accuracy_score(y_test, y_pred_tf)

print(f"TensorFlow model accuracy: {accuracy_tf}")

with torch.no_grad():
    X_test_pt = torch.tensor(X_test_scaled, dtype=torch.float32)
    y_pred_pt = torch.argmax(model_pt(X_test_pt), axis=1)
    accuracy_pt = accuracy_score(y_test, y_pred_pt)

print(f"PyTorch model accuracy: {accuracy_pt}")

