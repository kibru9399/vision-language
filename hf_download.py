from huggingface_hub import snapshot_download
import os

# The identifier of the model repository on Hugging Face Hub
model_id = "google/paligemma-3b-pt-224"

# Define the local directory where you want to save ALL the files
# Example: Creates a folder named "paligemma_local_files" in your current directory
local_directory = "./paligemma_local_files"

# Create the directory if it doesn't exist
os.makedirs(local_directory, exist_ok=True)

print(f"Downloading all files for {model_id} to {local_directory}...")

try:
    # This function downloads all files from the repo to your specified folder.
    # It handles the LFS files automatically.
    snapshot_download(
        repo_id=model_id,
        local_dir=local_directory,
        # Set to False to ensure actual files are copied, not symlinks (safer for portability)
        local_dir_use_symlinks=False,
        # Optional: Specify a revision (like a branch or commit hash) if needed
        # revision="main" # Or "bfloat16", etc. Defaults to 'main' usually.
    )
    print(f"Successfully downloaded all files to: {os.path.abspath(local_directory)}")

except Exception as e:
    print(f"An error occurred during download: {e}")
    print("Please check:")
    print("- Your internet connection.")
    print("- Permissions to write to the target directory.")
    print("- Available disk space (this model requires > 11 GB).")
    print("- If you need to log in to Hugging Face (try 'huggingface-cli login' in your terminal).")