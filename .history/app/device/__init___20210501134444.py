#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''
__auther__ = 'xwd'
# 测试该模块函数用
from flask import Blueprint
from flask_restful import Api
device = Blueprint('device',__name__,url_prefix='/device/')

from . import view
api = Api(device)
api.add_resource(view.Device_API,'device/<int:id>')
api.add_resource(view.welcome,'/')

def test():
    pass
if __name__ == '__main__':
    test()