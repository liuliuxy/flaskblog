import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


class BaseConfig(object):
    ASSETS_DEBUG = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    BLUELOG_POST_PER_PAGE = 5
    CKEDITOR_SERVE_LOCA = True
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'flaskblog.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG_MODE = 0


config = {

    'development': DevelopmentConfig
}
