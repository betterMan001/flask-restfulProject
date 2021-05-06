#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''
__auther__ = 'xwd'
# 测试该模块函数用
from flask import Blueprint

device = Blueprint('device',__name__,url_prefix='/device/')

from .views import *


def test():
    pass
if __name__ == '__main__':
    test()