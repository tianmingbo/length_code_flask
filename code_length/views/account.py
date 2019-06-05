from flask import Blueprint, request, render_template, session, redirect
from ..utils import helper
from ..utils.md5 import md5

account = Blueprint('account', __name__)


@account.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    username = request.form.get('user')
    pwd = request.form.get('pwd')
    pwd = md5(pwd)
    data = helper.fetch_one("select id,nickname from userinfo where user=%s and pwd=%s", (username, pwd))
    if not data:
        return render_template('login.html', error='用户名或密码错误')

    session['user_info'] = {'id': data['id'], 'nickname': data['nickname']}
    return redirect('/home')


@account.route('/loggout')
def logout():
    if 'user_info' in session:
        del session['user_info']
    return redirect('/login')
