# -*- coding: utf-8 -*-
"""DeiT_COCO.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YFHCyDpA_EbTy9j43sgIe4GQL4rSlrvf
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from torchvision import datasets, transforms
from torchvision.transforms import InterpolationMode
from timm import create_model
from sklearn.metrics import precision_recall_fscore_support, accuracy_score
import numpy as np
from tqdm import tqdm
import os

# Set random seed for reproducibility
torch.manual_seed(42)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Custom COCO Classification Dataset
class CocoClassification(Dataset):
    def __init__(self, root, annFile, transform=None):
        self.dataset = datasets.CocoDetection(root=root, annFile=annFile)
        self.transform = transform

        # Get categories from COCO dataset
        self.categories = self.dataset.coco.loadCats(self.dataset.coco.getCatIds())
        self.cat_ids = [cat['id'] for cat in self.categories]
        self.cat_id_to_label = {cat_id: i for i, cat_id in enumerate(self.cat_ids)}
        self.classes = [cat['name'] for cat in self.categories]

        # Filter images to only include those with annotations
        self.valid_ids = []
        for idx in range(len(self.dataset)):
            img, anns = self.dataset[idx]
            if len(anns) > 0:
                self.valid_ids.append(idx)

        print(f"Found {len(self.valid_ids)} images with annotations out of {len(self.dataset)} total images")

    def __getitem__(self, idx):
        # Get the image and annotations from the filtered indices
        real_idx = self.valid_ids[idx]
        img, anns = self.dataset[real_idx]

        # Get the primary category (use the first annotation's category)
        cat_id = anns[0]['category_id']
        label = self.cat_id_to_label[cat_id]

        # Apply transform if specified
        if self.transform is not None:
            img = self.transform(img)

        return img, label

    def __len__(self):
        return len(self.valid_ids)

# Define transforms
train_transform = transforms.Compose([
    transforms.Resize((224, 224), interpolation=InterpolationMode.BICUBIC),
    transforms.RandomHorizontalFlip(),
    transforms.RandomAutocontrast(),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

test_transform = transforms.Compose([
    transforms.Resize((224, 224), interpolation=InterpolationMode.BICUBIC),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Download COCO dataset if not present
print("Setting up COCO dataset...")
os.makedirs('./data/coco', exist_ok=True)

# Automatically download COCO dataset if not present
if not os.path.exists('./data/coco/annotations/instances_train2017.json'):
    print("Downloading COCO annotations...")
    !wget http://images.cocodataset.org/annotations/annotations_trainval2017.zip -P ./data/coco/
    !unzip -q ./data/coco/annotations_trainval2017.zip -d ./data/coco/

if not os.path.exists('./data/coco/train2017'):
    print("Downloading COCO train2017 images...")
    !wget http://images.cocodataset.org/zips/train2017.zip -P ./data/coco/
    !unzip -q ./data/coco/train2017.zip -d ./data/coco/

if not os.path.exists('./data/coco/val2017'):
    print("Downloading COCO val2017 images...")
    !wget http://images.cocodataset.org/zips/val2017.zip -P ./data/coco/
    !unzip -q ./data/coco/val2017.zip -d ./data/coco/

# COCO dataset paths
train_img_dir = './data/coco/train2017'
val_img_dir = './data/coco/val2017'
train_ann_file = './data/coco/annotations/instances_train2017.json'
val_ann_file = './data/coco/annotations/instances_val2017.json'

# Load COCO datasets
print("Loading COCO datasets...")
train_dataset = CocoClassification(root=train_img_dir, annFile=train_ann_file, transform=train_transform)
val_dataset = CocoClassification(root=val_img_dir, annFile=val_ann_file, transform=test_transform)

# Create data loaders - use the same batch size as in the original code
batch_size = 32
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=4)
val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=4)

# Create ViT model - COCO has 80 classes
model = create_model('deit_base_patch16_224', pretrained=True, num_classes=80)
model = model.to(device)

# Define loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.AdamW(model.parameters(), lr=1e-4, weight_decay=0.05)
scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=30)

def train_epoch(model, loader, criterion, optimizer):
    model.train()
    total_loss = 0
    correct = 0
    total = 0

    for images, targets in tqdm(loader, desc="Training"):
        images, targets = images.to(device), targets.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, targets)

        loss.backward()
        optimizer.step()

        total_loss += loss.item()
        _, predicted = outputs.max(1)
        total += targets.size(0)
        correct += predicted.eq(targets).sum().item()

    return total_loss / len(loader), 100. * correct / total

def evaluate(model, loader):
    model.eval()
    all_preds = []
    all_targets = []

    with torch.no_grad():
        for images, targets in tqdm(loader, desc="Evaluating"):
            images = images.to(device)
            outputs = model(images)
            _, predicted = outputs.max(1)

            all_preds.extend(predicted.cpu().numpy())
            all_targets.extend(targets.cpu().numpy())

    all_preds = np.array(all_preds)
    all_targets = np.array(all_targets)

    accuracy = accuracy_score(all_targets, all_preds)
    precision, recall, f1, _ = precision_recall_fscore_support(all_targets, all_preds, average='weighted')

    return accuracy, precision, recall, f1

# Training loop - keep the same number of epochs as the original code
num_epochs = 20
best_val_acc = 0

for epoch in range(num_epochs):
    train_loss, train_acc = train_epoch(model, train_loader, criterion, optimizer)
    val_acc, val_precision, val_recall, val_f1 = evaluate(model, val_loader)

    scheduler.step()

    print(f"Epoch {epoch+1}/{num_epochs}")
    print(f"Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.2f}%")
    print(f"Val Acc: {val_acc*100:.2f}%, Precision: {val_precision:.4f}, Recall: {val_recall:.4f}, F1: {val_f1:.4f}")

    # Save best model
    if val_acc > best_val_acc:
        best_val_acc = val_acc
        torch.save(model.state_dict(), 'best_coco_vit.pth')

# Load best model and evaluate on validation set (as test set)
model.load_state_dict(torch.load('best_coco_vit.pth'))
test_acc, test_precision, test_recall, test_f1 = evaluate(model, val_loader)

print("\nTest Set Results:")
print(f"Accuracy: {test_acc*100:.2f}%")
print(f"Precision: {test_precision:.4f}")
print(f"Recall: {test_recall:.4f}")
print(f"F1-score: {test_f1:.4f}")