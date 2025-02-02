import torch
import re
import torch.nn as nn
class NeuralNetwork(nn.Module):
    def __init__(self,input_size,hidden_size,num_classes):
        super(NeuralNetwork,self).__init__()
        self.l1=nn.Linear(input_size, hidden_size) #First Layer
        self.l2=nn.Linear(hidden_size, hidden_size) #Second Layer
        self.l3=nn.Linear(hidden_size, num_classes) #Output Layer
        self.relu=nn.ReLU() #Activation Function
    def forward(self,x):
        out=self.l1(x)
        out=self.relu(out)
        out=self.l2(out)
        out=self.relu(out)
        out=self.l3(out)
        return out
        