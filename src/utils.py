from pathlib import Path
import os, sys

def get_root_dir() -> Path:
    return Path(__file__).parent.parent

def get_modles_dir() -> Path:
    return Path(os.path.join(get_root_dir(), "models"))

def get_test_imgs_dir() -> Path:
    return Path(os.path.join(get_root_dir(), "test_imgs"))

def get_datasets_dir() -> Path:
    return Path(os.path.join(get_root_dir(), "datasets"))