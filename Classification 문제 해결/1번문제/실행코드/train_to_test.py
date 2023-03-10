import os
import sys

import pandas as pd

import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from torchvision import models

from timm.loss import LabelSmoothingCrossEntropy

from tqdm import tqdm

from custom_dataset import CustomDataset
from train_to_test_utils import set_augmentations, train, test
from timm.data import resolve_data_config
from timm.data.transforms_factory import create_transform
import timm

# Set Device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Set augmentations
train_transforms = set_augmentations('train')
valid_transforms = set_augmentations('valid')

# Load Dataset
dataset_path = os.path.join('../dataset')

train_dataset = CustomDataset(dataset_path, task='train', transforms=train_transforms)
# valid_dataset = CustomDataset(dataset_path, task='val', transforms=valid_transforms)
# test_dataset = CustomDataset(dataset_path, task='test', transforms=valid_transforms)

# Set DataLoader
train_loader = DataLoader(train_dataset, batch_size=40, shuffle=True, num_workers=4, pin_memory=True)
# valid_loader = DataLoader(valid_dataset, batch_size=40, shuffle=False, num_workers=4, pin_memory=True)
# test_loader = DataLoader(test_dataset, batch_size=1, shuffle=False, num_workers=4, pin_memory=True)
# print(len(train_dataset), '##', len(train_loader))
# exit()

# Call model
label_quantity = 10
model = models.densenet201()
# print(model.classifier) # Linear(in_features=1920, out_features=1000, bias=True)
model.classifier = nn.Linear(in_features=1920, out_features=label_quantity, bias=True)
# print(model.classifier)
model.to(device)
# print(model._get_name())
# exit()

# Set parameters
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=30, gamma=0.1)
epoch_num = 20

if __name__ == '__main__':
    # Train and validate
    train(train_loader, None, epoch_num, model, device, criterion, optimizer, scheduler)

    # Save last.pt
    torch.save(model.state_dict(), './last.pt')

    # test(test_loader, device, label_quantity)
