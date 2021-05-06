#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'包构建文件'
__auther__ = 'xwd'
# 测试该模块函数用
from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import *
db = SQLAlchemy()
def create_app(config_name):
    app =Flask(__name__)
    app.config.from_object(config.get(config_name))
    config.get(config_name).init_app(app)
    CORS(app,supports_credentials=True)
    db.init_app(app)
    from app.device import device
    app.register_blueprint(device)

    return app
def test():
    pass
if __name__ == '__main__':  
    test()