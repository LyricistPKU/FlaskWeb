# -*- encoding=UTF-8 -*-

from flask import Flask, render_template, request, make_response, redirect, flash, get_flashed_messages
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.jinja_env.line_statement_prefix = '#'
app.secret_key = 'FlaskTest'


@app.route('/index/')
@app.route('/')
def index():
    res = ''
    for msg, category in get_flashed_messages(with_categories=True):
        res = res + category + msg + '<br>'
    res += 'Hello'
    return res


@app.route('/profile/<int:uid>/')
def profile(uid):   # pass s user id
    # return 'profile:' + str(uid)
    # render_template来渲染模板
    colors = ('red', 'black')
    infos = {'Mike': 1, "Bob": 2, "Lucy": 3}
    return render_template('test.html', uid=uid, colors=colors, infos=infos)


@app.route('/request')
def request_demo():
    key = request.args.get('key', 'defaultkey')
    res = request.args.get('key', 'defaultkey') + '<br>'
    res = res + request.url + '++' + request.path + '<br>'
    for p in dir(request):
        res = res + str(eval('request...' + p)) + '<br>'
    respose = make_response(res)
    respose.set_cookie('userId', key)
    respose.status = '404'
    respose.headers['Hello'] = 'hello~~~'
    return respose


@app.route('/newpath')
def newpath():
    return 'newpath'


@app.route('/re/<int:code>')
def redirect_demo(code):
    return redirect('/newpath', code=code)


@app.errorhandler(404)
def page_not_found(error):
    print error
    return make_response('not_found.html')


@app.errorhandler(400)
def exception_handler(error):
    print error
    response = make_response('出错啦~')
    return response


@app.route('/admin')
def admin():
    key = request.args.get('key', 'defaultkey')
    if key == 'admin':
        return 'hello admin'
    else:
        raise Exception()
    return 'Uh oh!'


@app.route('/login')
def login():
    app.logger.info('log success')
    flash('登陆成功', 'info')   # flash利用session传消息
    return redirect('/')


@app.route('/log/<level>/<msg>/')
def log_test(level, msg):
    dict = {'warn': logging.WARN, 'error': logging.ERROR, 'info': logging.INFO}
    if level in dict.keys():
        app.logger.log(dict[level], msg)
    return 'logged:' + msg


def set_logger():
    info_file_handler = RotatingFileHandler('F:\\logs\\info.txt')
    info_file_handler.setLevel(logging.INFO)
    app.logger.addHandler(info_file_handler)

    warn_file_handler = RotatingFileHandler('F:\\logs\\warn.txt')
    warn_file_handler.setLevel(logging.WARN)
    app.logger.addHandler(warn_file_handler)

    error_file_handler = RotatingFileHandler('F:\\logs\\error.txt')
    error_file_handler.setLevel(logging.ERROR)
    app.logger.addHandler(error_file_handler)

if __name__ == '__main__':
    set_logger()
    app.run(debug=True)
