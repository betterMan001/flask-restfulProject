#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'设备相关api'
__auther__ = 'xwd'
from flask_restful import Resource
from flask import render_template
from app import db
from app.models import Device
from app.utils import BaseResponse

import traceback
res = BaseResponse()

class welcome(Resource):
    def get(self):
     return render_template('watchlist.html',user=user,movies=movies)
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