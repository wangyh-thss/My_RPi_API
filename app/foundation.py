# encoding=utf-8

from flask_login import LoginManager
from flask_wtf.csrf import CsrfProtect

login_manager = LoginManager()
csrf = CsrfProtect()
