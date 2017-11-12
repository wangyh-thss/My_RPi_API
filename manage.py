# encoding=utf-8

import json
from app import app
from flask_script import Server, Shell, Manager, prompt_bool

manager = Manager(app)


@manager.command
def runserver():
    app.debug = True
    # manager.run()
    # Server('127.0.0.1', port=8866)
    app.run()


if __name__ == "__main__":
    manager.run()
