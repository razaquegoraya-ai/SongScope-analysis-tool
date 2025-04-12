import os

class Config:
    DEBUG = False
    UPLOAD_FOLDER = 'uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    SECRET_KEY = os.urandom(24).hex()  # Generate a secure random key

class DevelopmentConfig(Config):
    DEBUG = True 