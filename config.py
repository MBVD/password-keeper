import os
from dotenv import load_dotenv

load_dotenv()
LOGGING_FILENAME = os.getenv("LOGGING_FILENAME")
CSV_FILE = os.getenv("CSV_FILE")