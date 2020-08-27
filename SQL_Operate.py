from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pymysql

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@127.0.0.1:3306/test"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+'./test.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECERET_KEY'] = 'saflm'

db = SQLAlchemy(app)

#学生表
class Student(db.Model):
    __tablename__ ='student'
    id = db.Column(db.Integer,primary_key=True)  #主键id
    name = db.Column(db.String(64),nullable=False)  #学生名不能为空
    gender = db.Column(db.Enum('男','女'),nullable=False)
    phone = db.Column(db.String(11),unique=True)  #手机号可以为空
    grades = db.relationship('Grade',backref='student')  #与成绩关联
    courses = db.relationship('Course',secondary='student_to_course',backref='students')  #与课程关联


#学生课程中间表
class StudentToCourse(db.Model):
    __tablename__ ='student_to_course'
    id = db.Column(db.Integer,primary_key=True)
    student_id = db.Column(db.Integer,db.ForeignKey('student.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))  # 所属课程


#课程表
class Course(db.Model):
    __tablename__ ='course'
    id = db.Column(db.Integer,primary_key=True)  #主键id
    name = db.Column(db.String(64),nullable=False)  #课程名不能为空
    grades = db.relationship('Grade',backref='course')  #与成绩关联
    teacher_id = db.Column(db.Integer,db.ForeignKey('teacher.id')) #所属教师
    # students = db.relationship('Student',secondary='student_to_course',backref='courses')  #与课程关联


#教师表
class Teacher(db.Model):
    __tablename__ ='teacher'
    id = db.Column(db.Integer,primary_key=True)  #主键id
    name = db.Column(db.String(64),nullable=False)  #教师名不能为空
    gender = db.Column(db.Enum('男','女'),nullable=False)
    phone = db.Column(db.String(11),unique=True)  #手机号可以为空
    course = db.relationship('Course',backref='teacher')  #与课程关联


#成绩表
class Grade(db.Model):
    __tablename__ ='grade'
    id = db.Column(db.Integer,primary_key=True)  #主键id
    # course_id =
    grade = db.Column(db.Integer,nullable=False)
    student_id = db.Column(db.Integer,db.ForeignKey('student.id')) #所属学生
    course_id = db.Column(db.Integer,db.ForeignKey('course.id')) #所属课程





if __name__ == '__main__':
    db.create_all()
    # db.drop_all()  #回调