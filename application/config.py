class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    HASH_NAME = 'sha256'
    HASH_SALT = b'VeryHardSalt'
    HASH_ITERATION = 100_000

    TOKEN_EXPIRE_MINUTES = 30
    TOKEN_EXPIRE_DAYS = 130
    JWT_ALGO = 'HS256'
    SECRET_KEY = 'VerySecretKey'