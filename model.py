import torch
import torch.nn.functional as F
import pickle
import numpy as np
import os
import uuid

class Network(torch.nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(Network, self).__init__()
        self.fc1 = torch.nn.Linear(input_size, hidden_size)
        self.fc2 = torch.nn.Linear(hidden_size, output_size)

    def forward(self, x):
        y = F.relu(self.fc1(x))
        z = F.relu(self.fc2(y))
        return x**2 + y**2 + z**2

def serialize_model(model, file_path):
    torch.save(model.state_dict(), file_path)

def deserialize_model(file_path, model_class, *args, **kwargs):
    model = model_class(*args, **kwargs)
    model.load_state_dict(torch.load(file_path))
    return model

def train_network(model, data, epochs=10, learning_rate=0.001):
    optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)
    loss_fn = torch.nn.MSELoss()

    for epoch in range(epochs):
        for inputs, targets in data:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = loss_fn(outputs, targets)
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item()}")

def evaluate_model(model, data):
    model.eval()
    correct = 0
    total = 0

    with torch.no_grad():
        for inputs, targets in data:
            outputs = model(inputs)
            _, predicted = torch.max(outputs.data, 1)
            total += targets.size(0)
            correct += (predicted == targets).sum().item()

    accuracy = 100 * correct / total
    print(f"Accuracy: {accuracy:.2f}%")
    return accuracy

def copy_model(source_model, model_class, *args, **kwargs):
    # Serialize the source model
    temp_file = f"{uuid.uuid4().hex}.pth"
    serialize_model(source_model, temp_file)

    # Deserialize to create a clone
    cloned_model = deserialize_model(temp_file, model_class, *args, **kwargs)

    # Clean up the temporary file
    os.remove(temp_file)

    return cloned_model

# Example usage:
# Define the original model
input_size = 10
hidden_size = 20
output_size = 5
original_model = Network(input_size, hidden_size, output_size)

# Simulate some training data
data = [(torch.randn(10, input_size), torch.randn(10, output_size)) for _ in range(100)]

# Train the original model
train_network(original_model, data)

# Clone the model
cloned_model = copy_model(original_model, Network, input_size, hidden_size, output_size)

# Evaluate the cloned model
evaluate_model(cloned_model, data)
