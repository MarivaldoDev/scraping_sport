import os
from dotenv import load_dotenv

load_dotenv()


SETTINGS = {
    "USER":os.getenv("USER", None),
    "PASSWORD":os.getenv("PASSWORD", None),
}