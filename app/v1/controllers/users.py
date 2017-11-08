# -*- coding:utf-8 -*-
from flask import Response
from . import *
from ..models.DbUser import DbUser
from ...api import requestParams

api = Blueprint('usersBlueprint', __name__)

@api.before_request
def validate():
    req = requestParams(request).validate()
    if req is not None:
        return req

# 用户中心首页
@api.route('/', methods = ['GET', 'POST'])
def lists():
    findall = DbUser.query.all()
    if findall is None:
        return Json().success(None)

    reqt = []
    for va in findall:
        reqt.append({'realname': va.realname, 'phone': va.phone})
    return Json().success(reqt)

# 单个用户信息
@api.route('/info', methods = ['POST'])
def info():
    account = request.values.get('account', None)
    if account is None:
        return Json().msg(500, 'account not none')

    user = DbUser.query.filter_by(account = account).first()
    if user is None:
        return Json().msg(500, 'account error')

    return Json().success({'realname': user.realname, 'phone': user.phone})
