import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

ZENOPAY_ACCOUNT_ID = os.getenv("ZENOPAY_ACCOUNT_ID")
ZENOPAY_API_KEY = os.getenv("ZENOPAY_API_KEY")
ZENOPAY_API_SECRET = os.getenv("ZENOPAY_API_SECRET")
    