#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'设备相关api'
__auther__ = 'xwd'
from flask_restful import Resource
from flask import render_template
from app import db
from app.models import Device
from app.utils import BaseResponse
from . import device
import traceback
res = BaseResponse()
user = {
    'username': 'Grey Li',
    'bio': 'A boy who loves movies and music.',
}

movies = [
    {'name': 'My Neighbor Totoro', 'year': '1988'},
    {'name': 'Three Colours trilogy', 'year': '1993'},
    {'name': 'Forrest Gump', 'year': '1994'},
    {'name': 'Perfect Blue', 'year': '1997'},
    {'name': 'The Matrix', 'year': '1999'},
    {'name': 'Memento', 'year': '2000'},
    {'name': 'The Bucket list', 'year': '2007'},
    {'name': 'Black Swan', 'year': '2010'},
    {'name': 'Gone Girl', 'year': '2014'},
    {'name': 'CoCo', 'year': '2017'},
]

# @device.route('/')
# def index():

#     return render_template('watchlist.html',user=user,movies=movies)

class welcome(Resource):
    def get(self):
        return 'hello'
class Device_API(Resource):
    def get(self,id):
        dev = Device.query.get(id)
        data = {
            'id':dev.id,
            'name':dev.name,
            'price':dev.price,
            'description':dev.description
        }
        return res.success(data=data)
    def delete(self,id):
        try:
            dev = Device.query.get(id)
            db.session.delete(dev)
            db.session.commit()
        except Exception as e:
            err_info = traceback.format_exc()
            print(err_info)
            return res.fail(msg=str(e))
        return res.success()
# 测试该模块函数用
def test():
    pass
if __name__ == '__main__':
    test()