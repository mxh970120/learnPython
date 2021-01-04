import mysql.connector

import mysql.connector
# 建立连接
conn = mysql.connector.connect(user='root', password='hao970120mxh')
# 建立对象
cursor = conn.cursor()
# 创建数据库:
# cursor.execute('create database python_test_1 charset=utf8')  # 已存在就跳过
cursor.execute('use python_test_1')
# 建立表，已存在就跳过
# cursor.execute('''create table students(
#                   id int unsigned primary key auto_increment not null,
#                   name varchar(20) default '',
#                   age tinyint unsigned default 0,
#                   height decimal(5,2),
#                   gender enum('男','女','中性','保密') default '保密',
#                   cls_id int unsigned default 0,
#                   is_delete bit default 0
#                   )''')

# cursor.execute('''insert into students values
#                 (0,'小明',18,180.00,2,1,0),
#                 (0,'小月月',18,180.00,2,2,1),
#                 (0,'彭于晏',29,185.00,1,1,0),
#                 (0,'刘德华',59,175.00,1,2,1),
#                 (0,'黄蓉',38,160.00,2,1,0),
#                 (0,'凤姐',28,150.00,4,2,1),
#                 (0,'王祖贤',18,172.00,2,1,1),
#                 (0,'周杰伦',36,NULL,1,1,0),
#                 (0,'程坤',27,181.00,1,2,0),
#                 (0,'刘亦菲',25,166.00,2,2,0),
#                 (0,'金星',33,162.00,3,3,1),
#                 (0,'静香',12,180.00,2,4,0),
#                 (0,'郭靖',12,170.00,1,4,0),
#                 (0,'周杰',34,176.00,2,5,0);''')
# 提交事务:
conn.commit()

# 运行查询,所有字段:
cursor.execute('select * from students;')
values = cursor.fetchall()
print(values)

# 运行查询，只名字:
cursor.execute('select name from students;')
values = cursor.fetchall()
print(values)

# 运行查询，as:
cursor.execute('select s.id,s.name,s.gender from students as s;')
values = cursor.fetchall()
print(values)

# 在select后面列前使用distinct可以消除重复的行:
cursor.execute('select distinct gender from students;')
values = cursor.fetchall()
print(values)




# 关闭Cursor和Connection:
cursor.close()

conn.close()