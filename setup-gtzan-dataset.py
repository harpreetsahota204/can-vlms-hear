import os
import shutil
import pandas as pd
import huggingface_hub

audio_datasets_path = "."

if not os.path.exists(audio_datasets_path):
    os.makedirs(audio_datasets_path, exist_ok=True)

huggingface_hub.snapshot_download(
    repo_id="MahiA/GT-Music-Genre", 
    repo_type="dataset", 
    local_dir=os.path.join(audio_datasets_path, "GT-Music-Genre")
    )


# Base directory
base_dir = "GT-Music-Genre"

# Create directory
save_dir = os.path.join(base_dir, "test")
os.makedirs(save_dir, exist_ok=True)

# Read the CSV file
df = pd.read_csv(os.path.join(base_dir, "test.csv"))

# Iterate through the DataFrame rows
for _, row in df.iterrows():
    # Get the source file path and genre
    source_file = os.path.join(base_dir, row['path'])
    genre = row['classname']
    filename = os.path.basename(source_file)
    
    # Create genre subdirectory inside train directory if it doesn't exist
    genre_dir = os.path.join(save_dir, genre)
    os.makedirs(genre_dir, exist_ok=True)
    
    # Define destination path
    dest_file = os.path.join(genre_dir, filename)
    
    # Move the file
    if os.path.exists(source_file):
        shutil.move(source_file, dest_file)
    else:
        print(f"Warning: File not found - {source_file}")

print("Files have been organized into genre subdirectories within the directory")