from functools import lru_cache

from PIL import Image

from config import PROFILE_PIC_FILE, RESUME_FILE


@lru_cache
def load_resume_bytes():
    return RESUME_FILE.read_bytes()


@lru_cache
def load_profile_pic():
    with Image.open(PROFILE_PIC_FILE) as image:
        return image.copy()
