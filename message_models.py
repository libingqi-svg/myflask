from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pymysql
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:1023@127.0.0.1:3306/school_messages"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+'./message.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECERET_KEY'] = 'saflm'
db = SQLAlchemy(app)  #实例化数据库

#管理员
class Admin(db.Model):
    __table_name__ = 'admin'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),nullable=False,unique=True)
    password = db.Column(db.String(64),nullable=False)
    tags = db.relationship('Tag',backref='admin')  #管理员与标签一对多

#标签
class Tag(db.Model):
    __table_name__ = 'tag'
    id = db.Column(db.Integer,primary_key=True)
    taglname = db.Column(db.String(10),nullable=False,unique=True)
    admin_id = db.Column(db.Integer,db.ForeignKey('admin.id'))

#用户
class User(db.Model):
    __table_name__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),nullable=False,unique=True)
    password = db.Column(db.String(64),nullable=False)
    mess = db.relationship('Message',backref='user')  #用户与留言一对多

#留言条
class Message(db.Model):
    __table_name__ = 'message'
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(256),nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    tags = db.relationship('Tag',secondary='message_to_tag',backref='messages')


#标签与留言中间表
class MessageToTag(db.Model):
    __tablename__ ='message_to_tag'
    id = db.Column(db.Integer,primary_key=True)
    message_id = db.Column(db.Integer,db.ForeignKey('message.id',ondelete='CASCADE'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id',ondelete='CASCADE'))

if __name__ == '__main__':
    db.create_all()
    # db.drop_all()  #回调

