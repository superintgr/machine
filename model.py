import torch

class Network(torch.nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(Network, self).__init__()
        self.fc1 = torch.nn.Linear(input_size, hidden_size)
        self.fc2 = torch.nn.Linear(hidden_size, output_size)

    def forward(self, x):
        y = torch.nn.functional.relu(self.fc1(x))
        z = torch.nn.functional.relu(self.fc2(y))
        i = x**2 + y**2 + z**2
        return torch.nn.functional.tanh(i)
