import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'defaultsecretkey')
    BACKEND_URL = os.getenv('FLASK_APP_URL', 'http://localhost:5000')
