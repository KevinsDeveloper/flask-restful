# -*- coding:utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))


# 基础配置
class Config:
    SSL_DISABLE = True

    @staticmethod
    def init_app(app):
        pass


# 开发环境
class Development(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JSON_AS_ASCII = False

    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASS = 'q1w2e3456'
    DB_NAME = 'phalcon'
    # mysql
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{USER}:{PASS}@{ADDR}/{NAME}".format(USER=DB_USER, PASS=DB_PASS, ADDR=DB_HOST, NAME=DB_NAME)


# 生产环境
class Production(Config):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JSON_AS_ASCII = False

    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASS = 'powerdev'
    DB_NAME = 'phalcon'

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{USER}:{PASS}@{ADDR}/{NAME}".format(USER=DB_USER, PASS=DB_PASS, ADDR=DB_HOST, NAME=DB_NAME)


config = {
    'development': Development,
    'production': Production
}
