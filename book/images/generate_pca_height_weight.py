"""
Generate a 2D visualization of PCA using height vs weight example.
Shows original axes and principal component axes.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import seaborn as sns

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 5)
plt.rcParams['font.size'] = 11

# Set random seed for reproducibility
np.random.seed(42)

# Generate correlated height and weight data
n_samples = 100

# Heights (in inches, centered around 67 inches / 5'7")
heights = np.random.normal(67, 4, n_samples)

# Weights (in lbs, correlated with height)
# Base weight + effect of height + random variation
weights = 50 + 3 * heights + np.random.normal(0, 10, n_samples)

# Combine into a matrix
X = np.column_stack([heights, weights])

# Standardize the data (mean=0, std=1) for clearer visualization
X_mean = X.mean(axis=0)
X_centered = X - X_mean
X_std = X_centered / X_centered.std(axis=0)

# Apply PCA
pca = PCA(n_components=2)
pca.fit(X_std)

# Get principal components (these are the eigenvectors)
pc1 = pca.components_[0]
pc2 = pca.components_[1]

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- LEFT PLOT: Original axes with PC directions overlaid ---
ax1.scatter(X_std[:, 0], X_std[:, 1], alpha=0.6, s=50, color='steelblue',
            edgecolors='navy', linewidth=0.5)

# Draw original axes
ax1.axhline(y=0, color='gray', linestyle='--', linewidth=1, alpha=0.5)
ax1.axvline(x=0, color='gray', linestyle='--', linewidth=1, alpha=0.5)

# Draw PC1 (first principal component) - scaled for visibility
scale_factor = 2.5
ax1.arrow(0, 0, pc1[0]*scale_factor, pc1[1]*scale_factor,
          head_width=0.15, head_length=0.1, fc='red', ec='red', linewidth=3,
          label='PC1 (Max Variance)', length_includes_head=True, zorder=5)

# Draw PC2 (second principal component)
ax1.arrow(0, 0, pc2[0]*scale_factor, pc2[1]*scale_factor,
          head_width=0.15, head_length=0.1, fc='orange', ec='orange', linewidth=3,
          label='PC2 (Perpendicular)', length_includes_head=True, zorder=5)

# Labels and formatting
ax1.set_xlabel('Height (standardized)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Weight (standardized)', fontsize=12, fontweight='bold')
ax1.set_title('Original Data with Principal Components\n(PC1 captures "overall size", PC2 captures "body type")',
              fontsize=13, fontweight='bold', pad=15)
ax1.legend(loc='upper left', fontsize=11, frameon=True, shadow=True)
ax1.grid(True, alpha=0.3)
ax1.set_xlim(-3, 3)
ax1.set_ylim(-3, 3)

# Add text annotations
ax1.text(1.8, 1.8, 'Tall &\nHeavy', fontsize=10, ha='center',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
ax1.text(-1.8, -1.8, 'Short &\nLight', fontsize=10, ha='center',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
ax1.text(1.5, -1.5, 'Tall &\nSlim', fontsize=9, ha='center', alpha=0.7)
ax1.text(-1.5, 1.5, 'Short &\nStocky', fontsize=9, ha='center', alpha=0.7)

# --- RIGHT PLOT: Data in PC coordinate system ---
# Transform data to PC space
X_pca = pca.transform(X_std)

ax2.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.6, s=50, color='forestgreen',
            edgecolors='darkgreen', linewidth=0.5)

# Draw PC axes (now aligned with x and y)
ax2.axhline(y=0, color='orange', linestyle='--', linewidth=2, alpha=0.7, label='PC2 axis')
ax2.axvline(x=0, color='red', linestyle='--', linewidth=2, alpha=0.7, label='PC1 axis')

# Labels and formatting
ax2.set_xlabel('PC1 (Overall Size)', fontsize=12, fontweight='bold')
ax2.set_ylabel('PC2 (Body Type: Stocky ← → Slim)', fontsize=12, fontweight='bold')
ax2.set_title('Data Projected onto Principal Components\n(Rotated coordinate system)',
              fontsize=13, fontweight='bold', pad=15)
ax2.legend(loc='upper right', fontsize=11, frameon=True, shadow=True)
ax2.grid(True, alpha=0.3)
ax2.set_xlim(-3, 3)
ax2.set_ylim(-3, 3)

# Add variance explained
variance_explained = pca.explained_variance_ratio_ * 100
ax2.text(0.02, 0.98, f'PC1 explains {variance_explained[0]:.1f}% of variance\nPC2 explains {variance_explained[1]:.1f}% of variance',
         transform=ax2.transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()

# Save the figure
plt.savefig('/Users/boehmkbc/Desktop/Brads-Folder/UC/uc-bana-4080/book/images/31-pca-height-weight-intuition.png',
            dpi=300, bbox_inches='tight', facecolor='white')

print("✓ Figure saved: 31-pca-height-weight-intuition.png")
print(f"  - PC1 explains {variance_explained[0]:.1f}% of variance")
print(f"  - PC2 explains {variance_explained[1]:.1f}% of variance")

plt.show()
