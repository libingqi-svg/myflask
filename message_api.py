from message_models import app,db,Admin,Message,Tag,User
from flask import jsonify,session,request

app.secret_key = 'sdasfljs3zs6'
@app.route('/index')
@app.route('/')
def hello_word():
    return 'hello'

#管理员初始化
@app.route('/init/admin')
def init_admin():
    """
    账号:admin
    密码:default
    """
    admin = Admin(username='admin',password='default')
    try:
        db.session.add(admin)
        db.session.commit()
        return jsonify(code=200,msg='初始化成功')
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400,msg='初始化失败')

#管理员登录
@app.route('/admin/login',methods=['POST'])
def login_admin():
    req_data = request.get_json()
    username = req_data.get('username')
    password = req_data.get('password')
    if not all([username,password]):
        return jsonify(code=400,msg='参数不完整')
    admin = Admin.query.filter(Admin.username == username).first()
    #验证管理员的账号和密码
    if admin is None or password != admin.password:
        return jsonify(code=400,msg='账号或密码错误')
    session['admin_name'] = username
    session['admin_id'] = admin.id
    return jsonify(msg = '登录成功')

#检查管理员登录状态
@app.route('/admin/session',methods=['GET'])
def check_admin_sess():
    admin_id = session.get('admin_id')
    admin_name = session.get('admin_name')
    if admin_id is not None:
        return jsonify(admin_id=admin_id,admin_name=admin_name)
    else:
        return jsonify(msg = '没登录,请先登录')

#管理员退出登录
@app.route('/admin/logout')
def logout_admin():
    session.clear()
    return jsonify(msg='成功退出！')

#管理员增标签
@app.route('/admin/tag',methods=['POST'])
def admin_add_tag():
    req_data = request.get_json()
    tag_name = req_data.get('tag_name')
    admin_id = session.get('admin_id')
    if not all([tag_name,admin_id]):
        return jsonify(code=400,msg='参数不完整或未登录')
    tag =Tag(taglname=tag_name,admin_id=admin_id)
    try:
        db.session.add(tag)
        db.session.commit()
        return jsonify(code=200,msg='添加标签成功')
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400,msg='添加标签失败')

#管理员删标签
@app.route('/admin/tag',methods=['DELETE'])
def admin_delete_tag():
    req_data = request.get_json()
    tag_name = req_data.get('tag_name')
    admin_id = session.get('admin_id')
    if not all([tag_name, admin_id]):
        return jsonify(code=400, msg='参数不完整或未登录')
    try:
        tag = Tag.query.filter(Tag.taglname == tag_name).delete()
        db.session.commit()
        return jsonify(code=200, msg='删除标签成功')
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg='删除标签失败')

#管理员删留言
@app.route('/admin/message',methods=['DELETE'])
def admin_delete_message():
    req_data = request.get_json()
    message_id = req_data.get('message_id')
    admin_id = session.get('admin_id')
    if not all([message_id, admin_id]):
        return jsonify(code=400, msg='参数不完整')
    msg = Message.query.get(id)
    if msg is None:
        return jsonify(code=400, msg='留言不存在,无法删除')

    try:
        m = Message.query.filter(Message.id == message_id).delete()
        db.session.commit()
        return jsonify(code=200, msg='删除成功')
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg='删除失败')


#用户注册
@app.route('/user/register',methods=['POST'])
def user_register():
    req_data = request.get_json()
    username = req_data.get('username')
    password = req_data.get('password')
    user =  User(username = username,password=password)
    try:
        db.session.add(user)
        db.session.commit()
        return jsonify(code=200, msg='用户注册成功')
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg='用户注册失败')

#用户登录
@app.route('/user/login',methods=['POST'])
def user_login():
    req_data = request.get_json()
    username = req_data.get('username')
    password = req_data.get('password')
    if not all([username, password]):
        return jsonify(code=400, msg='参数不完整')
    user = User.query.filter(User.username == username).first()
    # 验证用户的账号和密码
    if user is None or password != user.password:
        return jsonify(code=400, msg='账号或密码错误')
    session['user_name'] = username
    session['user_id'] = user.id
    return jsonify(msg='登录成功')

#检查用户登录状态
@app.route('/user/session',methods=['GET'])
def check_user_sess():
    user_id = session.get('user_id')
    user_name = session.get('user_name')
    if user_id is not None:
        return jsonify(user_id=user_id,user_name=user_name)
    else:
        return jsonify(msg = '没登录,请先登录')

#用户退出登录
@app.route('/user/logout')
def user_logout():
    session.clear()
    return jsonify(msg='成功退出！')

#用户发布留言
@app.route('/user/message',methods=['POST'])
def user_post_message():
    req_data = request.get_json()
    user_id = session.get('user_id')
    content = req_data.get('content')
    tags = req_data.get('tags')
    if not all([user_id,content,tags]):
        return jsonify(code=400,msg='参数不完整')
    try:
        tags = Tag.query.filter(Tag.taglname.in_(tags)).all()
        message = Message(content=content,user_id=user_id)
        message.tags = tags
        db.session.add(message)
        db.session.commit()
        return jsonify(code=200, msg='发布留言成功')
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400,msg='发布留言失败')

#用户删除留言
@app.route('/user/message',methods=['DELETE'])
def user_delete_message():
    req_data = request.get_json()
    message_id = req_data.get('message_id')
    user_id = session.get('user_id')
    if not all([message_id,user_id]):
        return jsonify(code=400,msg='参数不完整')
    msg = Message.query.get(message_id)
    if msg is None:
        return jsonify(code=400,msg='留言不存在,无法删除')
    if user_id !=msg.user_id:
        return jsonify(code=400,msg='你不是作者,无法删除')
    try:
        m = Message.query.filter(Message.id == message_id).delete()
        db.session.commit()
        return jsonify(code=200, msg='删除成功')
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400,msg='删除失败')

#用户查看留言记录
@app.route('/user/message/history')
def user_messages_history():
    user_id = session.get('user_id')
    if user_id is None:
        return jsonify(code=400,msg='请登录')
    user = User.query.get(user_id)
    if user is None:
        return jsonify(code=400,msg='用户不存在')

    #获取留言
    historys = []
    messages = user.mess
    for message in messages:
        content = message.content
        tags = message.tags
        tag_names = []
        for tag in tags:
            tag_names.append(tag.taglname)
        create_time = message.create_time.strftime("%Y-%m-%d %H:%M:%S")
        user_id = message.user_id
        data = {'content':content,
                'message_id':message.id,
                'tags':tag_names,
                'create_time':create_time,
                'user_id':user_id}
        historys.append(data)
    return jsonify(code=200,msg='查询成功',data = historys)

#留言板所有公共留言
@app.route('/user/message/board')
def user_messages_board():
    messages = Message.query.all()
    historys=[]
    for message in messages:
        content = message.content
        tags = message.tags
        tag_names = []
        for tag in tags:
            tag_names.append(tag.taglname)
        create_time = message.create_time.strftime("%Y-%m-%d %H:%M:%S")
        user_id = message.user_id
        data = {'content':content,
                'message_id':message.id,
                'tags':tag_names,
                'create_time':create_time,
                'user_id':user_id}
        historys.append(data)
    return jsonify(code=200,msg='查询成功',data = historys)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)