class Config:
    DEBUG = False
    UPLOAD_FOLDER = 'uploads/'
    MAX_CONTENT_LENGTH = 32 * 1024 * 1024  # 32MB limit
    SECRET_KEY = 'replace-with-random-string-in-production'

class DevelopmentConfig(Config):
    DEBUG = True 