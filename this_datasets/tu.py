import matplotlib.pyplot as plt
import numpy as np

# Set font for SCI papers
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 12

# Data preparation
categories = ['Boeing787', 'Boeing737', 'A330', 'other', 'A220', 'ARJ21', 'A320/321']
train_counts = [2399, 2288, 279, 3786, 3372, 1039, 1598]
val_counts = [517, 569, 63, 739, 741, 199, 354]

# Calculate positions and width
x = np.arange(len(categories))
width = 0.35

# Create figure
plt.figure(figsize=(14, 8))

# Plot bar charts
bars1 = plt.bar(x - width/2, train_counts, width, label='Training Set',
                color='skyblue', edgecolor='navy', alpha=0.8)
bars2 = plt.bar(x + width/2, val_counts, width, label='Validation Set',
                color='lightcoral', edgecolor='darkred', alpha=0.8)

# Set chart properties
plt.xlabel('Aircraft Categories', fontsize=14, fontweight='bold')
plt.ylabel('Number of Annotations', fontsize=14, fontweight='bold')
plt.title('Class Distribution Comparison in SAR-Aircraft-1.0 Dataset',
          fontsize=16, fontweight='bold', pad=20)
plt.xticks(x, categories, rotation=45)
plt.legend(fontsize=12)

# Add value labels on bars
def add_value_labels(bars):
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 30,
                f'{int(height)}', ha='center', va='bottom',
                fontsize=10, fontweight='bold')

add_value_labels(bars1)
add_value_labels(bars2)

# Add grid lines for better readability
plt.grid(axis='y', alpha=0.3, linestyle='--')

# Adjust layout
plt.tight_layout()

# Save figure for SCI paper
plt.savefig('class_imbalance_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# Statistical analysis
print("=" * 70)
print("DETAILED CLASS IMBALANCE ANALYSIS OF SAR-AIRCRAFT-1.0 DATASET")
print("=" * 70)

train_total = sum(train_counts)
val_total = sum(val_counts)

print("\nClass Distribution Percentage Analysis:")
print("-" * 65)
print(f"{'Category':<12} {'Train':<8} {'Ratio':<8} {'Val':<8} {'Ratio':<8} {'Total':<8}")
print("-" * 65)

for i, category in enumerate(categories):
    train_pct = (train_counts[i] / train_total) * 100
    val_pct = (val_counts[i] / val_total) * 100
    total = train_counts[i] + val_counts[i]
    print(f"{category:<12} {train_counts[i]:<8} {train_pct:>5.1f}% {val_counts[i]:<8} {val_pct:>5.1f}% {total:<8}")

# Imbalance analysis
max_train = max(train_counts)
min_train = min(train_counts)
max_val = max(val_counts)
min_val = min(val_counts)

print(f"\nImbalance Analysis:")
print(f"Training Set - Max: {max_train}({categories[train_counts.index(max_train)]}) | "
      f"Min: {min_train}({categories[train_counts.index(min_train)]}) | "
      f"Imbalance Ratio: {max_train/min_train:.2f}:1")

print(f"Validation Set - Max: {max_val}({categories[val_counts.index(max_val)]}) | "
      f"Min: {min_val}({categories[val_counts.index(min_val)]}) | "
      f"Imbalance Ratio: {max_val/min_val:.2f}:1")

print(f"\nTotal Samples: {train_total + val_total} (Training: {train_total}, Validation: {val_total})")

# Identify problematic categories
print(f"\nCategories Requiring Special Attention:")
print(f"- A330: Minimum samples, only {min_train} in training and {min_val} in validation")
print(f"- ARJ21: Limited samples, {1039} in training and {199} in validation")
print(f"- A320/321: Moderate samples, {1598} in training and {354} in validation")

# Additional statistical metrics
print(f"\nAdditional Statistical Metrics:")
print(f"Training set standard deviation: {np.std(train_counts):.2f}")
print(f"Validation set standard deviation: {np.std(val_counts):.2f}")
print(f"Coefficient of variation (Training): {(np.std(train_counts)/np.mean(train_counts))*100:.2f}%")
print(f"Coefficient of variation (Validation): {(np.std(val_counts)/np.mean(val_counts))*100:.2f}%")