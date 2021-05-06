#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'公用工具类模块'
__auther__ = 'xwd'
# 测试该模块函数用
from flask import jsonify
class BaseResponse:
    def __init__(self):
        self.result_code_success = 0
        self.result_code_fail = 1

    def success(self, msg='success', data={}):
        result = {'status': self.result_code_success, 'msg': msg, 'data': data}

        return jsonify(result)

    def fail(self, msg='fail', data={}):
        result = {'status': self.result_code_fail, 'msg': msg, 'data': data}

        return jsonify(result)
        
def test():
    pass
if __name__ == '__main__':
    test()