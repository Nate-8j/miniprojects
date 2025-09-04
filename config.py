import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

KEY = os.getenv("ACCESS_KEY")
