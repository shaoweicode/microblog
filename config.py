#激活（跨站点请求伪造）保护
CSRF_ENABLED =  True
#建立加密令牌用于验证一个表单
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS=[
    {'name':'Google','url':'https://www.google.com/accounts/o8/id'},
    {'name':'Yahoo','url':'https://me.yahoo.com'},
    {'name':'AOL','url':'https://www.flicker.com/<username>'},
    {'name':'MyOpenID','url':'https://www.openid.com'}
]

import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir,'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_respository')