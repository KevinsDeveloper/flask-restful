# -*- coding:utf-8 -*-
from .. import *

class DbUser(db.Model):
    __tablename__ = 'db_auth_user'

    # 主键ID
    id = db.Column(db.Integer, primary_key = True)
    # 账号
    account = db.Column(db.String(100), unique = True)
    # 姓名
    realname = db.Column(db.String(100), nullable = False)
    # 手机
    phone = db.Column(db.String(100))

    def __init__(self, account, realname):
        self.account = account
        self.realname = realname

    def __repr__(self):
        return '<Account %r>' % self.account
