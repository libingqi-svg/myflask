from SQL_Operate import db,Student,Grade,Teacher,Course

# 一.增
# s = Student(name='张三',gender='男',phone='12456789311')
# s1 = Student(name='张四',gender='男',phone='12456789313')
# s2 = Student(name='张是',gender='男',)
# s3 = Student(name='张有',gender='女',phone='12456789312')

#执行语句
# db.session.add(s1)
# db.session.add(s2)
# db.session.add(s3)
# db.session.add_all([s,s1,s2,s3])  #批量添加
#提交语句
# db.session.commit()


# 二.查
#1.通过id单个查询
# stu = Student.query.get(1)  #get(id)
# print(stu.name)
# print(stu.gender)

#2.查询全部
# stu1 = Student.query.all()
# for i in stu1:
#     print(i.name,i.gender,i.phone)

#3.filter条件查询
# stu2 = Student.query.filter(Student.id>=3)   #Student.name=='张三'
# for i in stu2:
#     print(i.name,i.id)

#4.filter_by() 查询  类似于 select * from 语句
# stu3 = Student.query.filter_by(name='张三').filter(Student.id==1)       #.first()返回第一个  .all()返回全部
# for i in stu3:
#     print(i.name)
# print(stu3)


# 三.改
#1.
# stu4 = Student.query.filter(Student.id==1).update({'name':'张译'})
# db.session.commit()

# stu4 = Student.query.filter(Student.gender=='男').update({'gender':'女'})
# print(stu4)
# db.session.commit()

#2.
# stu5 = Student.query.filter(Student.gender=='女').first()
# stu5.gender = '男'
# db.session.add(stu5)

# stu6 = Student.query.filter(Student.gender=='女').all()
# for i in stu6:
#     i.gender = '男'
#     db.session.add(i)
# db.session.commit()



# 四.删
# stu7 = Student.query.filter(Student.id==3).delete()
# print(stu7)
# db.session.commit()

'''-------------------------------'''
# grade1 = Grade(grade=100,student_id=1)
# grade2 = Grade(grade=90,student_id=1)
# grade3 = Grade(grade=80,student_id=1)
# db.session.add_all([grade1,grade2,grade3])
# db.session.commit()

# #通过设置学生id 查找学生成绩(没有体现出1对多)
# grade = Grade.query.filter(Grade.student_id==1).all()
# for i in grade:
#     print(i.grade)

#通过1访问多
# stu = Student.query.get(1)
# for i in stu.grades:
#     print(stu.name,i.grade)

# #通过多访问1
# grade = Grade.query.filter(Grade.grade=='100').all()
# for i in grade:
#     print(i.student.name,i.student.gender)



#多对多操作
# s0 = Student(name='李一',gender='男',phone='12456789311')
# s1 = Student(name='李二',gender='女',phone='12456789313')
# s2 = Student(name='李三',gender='男',)
# s3 = Student(name='李四',gender='女',phone='12456789312')
# s4 = Student(name='李五',gender='男',phone='12456789411')
# s5 = Student(name='李留',gender='女',phone='12456779313')
# s6 = Student(name='李期',gender='男',)
# s7 = Student(name='李吧',gender='女',phone='12556789312')
#
# t1 = Teacher(name='老数',gender='男',phone='11122233344')
# t2 = Teacher(name='老外',gender='女',phone='11192233344')
# t3 = Teacher(name='老语',gender='女',phone='11892233344')
# t4 = Teacher(name='老物',gender='男',phone='11782233344')
#
# c1 = Course(name='数学')
# c2 = Course(name='语文')
# c3 = Course(name='英语')
# c4 = Course(name='物理')
#
# db.session.add_all([s0,s1,s2,s3,s4,s5,s6,s7,t1,t2,t3,t4,c1,c2,c3,c4])  #批量添加
# db.session.commit()# 提交语句

# for i in range(1,5):
#     c = Course.query.filter(Course.id==i).update({'teacher_id':i})
# db.session.commit()

#查询课程表
cs = Course.query.filter(Course.id>=2).all()
# for c in cs:
#     print(c.name)

stu = Student.query.filter(Student.id>=2).all()
for s in stu:
    s.courses = cs
    db.session.add(s)
db.session.commit()

#学生查询课程
stu = Student.query.get(1)
for c in stu.courses:
    print(c.name)

#课程查询学生
cs = Course.query.get(2)
for s in cs.students:
    print(s.name)