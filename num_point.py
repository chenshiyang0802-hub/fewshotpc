import os
import numpy as np

# Path to your folder containing all .npy files
folder = '/home/zychen/Documents/Project_shno/fewshotpc/datasets/S3DIS/scenes/blocks_bs1_s1/data'

# Collect all .npy files in that directory
files = [f for f in os.listdir(folder) if f.endswith('.npy')]

total_points = 0
num_files = 0

for filename in files:
    path = os.path.join(folder, filename)
    data = np.load(path)
    num_points = data.shape[0]   # number of points in that block
    total_points += num_points
    num_files += 1

mean_points = total_points / num_files if num_files > 0 else 0
print(f"Processed {num_files} blocks")
print(f"Average number of points per block: {mean_points:.2f}")