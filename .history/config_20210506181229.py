#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'配置类'
__auther__ = 'xwd'
import os
from os.path import join 
basedir = os.path.abspath(os.path.dirname(__file__))
# 测试该模块函数用
def test():
    pass
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMI_ONTEARDOWN = True #请求成功后会自动提交数据库中的变动
    @staticmethod  #静态方法
    def init_app(app):
        pass
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://learn:xwd851428195@localhost:3306/devicemanage'
class TestingConfig(Config):
    TESING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://learn:xwd851428195@localhost:3306/devicemanage'

class ProductionConfig(Config):  
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://learn:xwd851428195@localhost:3306/devicemanage'

config = {
'development':DevelopmentConfig,
'testing':TestingConfig,
'production':ProductionConfig,
'default': DevelopmentConfig
}