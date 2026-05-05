import shutil
from pathlib import Path
from huggingface_hub import HfApi
import os

TOKEN = "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"
REPO_ID = "rajadityaaaaaa/file2-openenv"
SPACE_DIR = Path(r"c:\Users\WIN11\Downloads\file 2i\FILE2\FILE2\hf_space")
BACKEND_DIR = Path(r"c:\Users\WIN11\Downloads\file 2i\FILE2\FILE2\backend")

def sync_folders():
    print("Synchronizing HF Space folder with latest Backend code...")
    folders_to_sync = ["core", "api", "services", "static"]
    for folder in folders_to_sync:
        src = BACKEND_DIR / folder
        dst = SPACE_DIR / folder
        if src.exists():
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
            print(f"  - Synced {folder}/")
        else:
            print(f"  - Skipping {folder}/ (not found in source)")

# Run Sync
sync_folders()

api = HfApi(token=TOKEN)

# Create space if it doesn't exist
try:
    api.create_repo(
        repo_id=REPO_ID,
        repo_type="space",
        space_sdk="docker",
        private=False,
        exist_ok=True,
    )
    print(f"Space created/verified: {REPO_ID}")
except Exception as e:
    print(f"Repo note: {e}")

# Upload all files
print("Uploading files to Hugging Face...")
api.upload_folder(
    folder_path=str(SPACE_DIR),
    repo_id=REPO_ID,
    repo_type="space",
    ignore_patterns=["__pycache__", "*.pyc", ".git", "*.pyo"],
)
print(f"\nDEPLOYED! Visit: https://huggingface.co/spaces/{REPO_ID}")
print(f"Live API:  https://{REPO_ID.replace('/', '-')}.hf.space")
