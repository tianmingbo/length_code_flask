from flask import Blueprint, request, render_template, session, redirect
from ..utils import helper
import uuid, os

ind = Blueprint('index', __name__)


@ind.before_request
def process_request():
    if not session.get('user_info'):
        return redirect('/login')
    return None


@ind.route('/home')
def home():
    return render_template('home.html')


@ind.route('/user_list')
def user_list():
    user_list = helper.fetch_all('select id ,user,nickname from userinfo', [])
    return render_template('list.html', user_list=user_list)


@ind.route('/detail/<int:id>')
def detail(id):
    record_list = helper.fetch_all('select id , line, ctime from record where user_id=%s', (id,))
    return render_template('detail.html', record_list=record_list)


@ind.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    file_obj = request.files.get('code')

    # 检查上传文件的后缀名
    name_dis = file_obj.filename.rsplit('.', maxsplit=1)
    if len(name_dis) != 2:
        return "请上传zip文件"
    if name_dis[1] != 'zip':
        return "请上传zip文件"

    # 接受用户上传文件，并解压到指定目录
    import zipfile
    target_path = os.path.join('files', str(uuid.uuid4()))
    file_path = os.path.join('files', file_obj.filename)
    file_obj.save(file_path)

    f = zipfile.ZipFile(file_path, 'r')
    for file in f.namelist():
        f.extract(file, target_path)

    # 遍历目录下的所有文件
    total_num = 0
    for base_path, folder_list, file_list in os.walk(target_path):  # 路径、文件夹、文件
        for file_name in file_list:
            file_path = os.path.join(base_path, file_name)  # 每一个文件
            file_dis = file_path.rsplit('.', maxsplit=1)
            if len(file_dis) != 2:
                continue
            if file_dis[1] != 'py':
                continue
            file_num = 0
            with open(file_path, 'rb')as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    if line.startswith(b'#'):
                        continue
                    file_num += 1
            total_num += file_num
    import datetime
    ctime = datetime.date.today()
    data = helper.fetch_one("select id from record where ctime=%s and user_id=%s", (ctime, session['user_info']['id']))
    if data:
        return '今天已经上传'
    helper.insert("insert into record(line,ctime,user_id)values(%s,%s,%s)",
                  (total_num, ctime, session['user_info']['id']))
    return "上传成功"
