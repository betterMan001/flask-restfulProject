#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'orm对象'
__auther__ = 'xwd'
from app import db
class Device(db.Model):
    __tablename__ ='device'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(22))
    price = db.Column(db.Float)
    classId = db.Column(db.Integer,nullable=False,index=True)
    description = db.Column(db.String(200))
class DeviceClass(db.Model):
    __tablename__ ='deviceclass'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20))

# 测试该模块函数用
def test():
    pass
if __name__ == '__main__':
    test()