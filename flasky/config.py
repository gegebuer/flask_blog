import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <952997972@qq.com>'
    FLASKY_ADMIN = '18521501127@139.com'
    
    @staticmethod
    def init_app(app):
        pass
        
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATEBASE_URI = os.environ.get('DEV_DATABASE_URL') or 'mysql://root:jianggege0323@localhost/python_db'
    
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATEBASE_URI = os.environ.get('TEST_DATABASE_URL') or 'mysql://root:jianggege0323@localhost/test_db'
    
class ProductionConfig(Config):
    SQLALCHEMY_DATEBASE_URI = os.environ.get('DATABASE_URL') or 'mysql://root:jianggege0323@localhost/python_db'
    
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    
    'default': DevelopmentConfig
}