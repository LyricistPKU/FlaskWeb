# -*- encoding=UTF-8 -*-
from flask_script import Manager
from FlaskTest import app

manager = Manager(app)


@manager.option('-n',  '--name', dest='name', default='nowcoder')
def hello(name):    # 定义在shell中可传入的参数
    '-n dest=name --name default=nowcoder'
    print 'hello', name


@manager.command
def initialize_database():
    'initialize database'
    print 'database ...'    # 对可传入参数的描述

if __name__ == '__main__':
    manager.run()
