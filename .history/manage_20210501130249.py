#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'贴模板用的'
__auther__ = 'xwd'
from flask_script import Manager,Shell
from app import create_app,db
import os
from dotenv import load_dotenv
from app.models import Device,DeviceClass
from flask_migrate import Migrate,MigrateCommand

load_dotenv()
app = create_app(os.getenv('FLASK_ENV') or'default')
manager = Manager(app)
migrate =Migrate(app,db)
def make_shell_context():
    return dict(db=db)
manager.add_command('shell',Shell(make_context=make_shell_context))
manager.add_command('db',MigrateCommand)
@manager.command
def routes(): #函数名就是命令
    #显示系统的路由表
    print([ rule for rule in app.url_map.iter_rules()])
# 测试该模块函数用
def test():
    pass
if __name__ == '__main__':
    manager.run()