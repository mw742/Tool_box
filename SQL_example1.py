import MySQLdb

#######################################################
######第一步，链接数据库#######
#######################################################
## 创建一个connection 对象，代表了一个数据库链接
connection=MySQLdb.connect(
    host='123.345.678',#数据库Ip地址
    user='user1',#mysql用户名
    password='123456',#mysql用户名登陆密码
    db='byhy',#数据库名
    #如果数据库里面的文本是utf8编码的，
    #charset指定是utf8
    charset='utf8'
)


#######################################################
######第二步，链接数据库之后干事情########
#######################################################
##返回一个cursor对象
#变量名为c
c=connection.cursor()


#######################################################
##第三步，获取数据库中的数据，查询的数据#####
#######################################################
##执行一个获取users表中所记录的sql语句
##双引号中的就是sql语句，通过这种方式python可以执行sql语句
c.execute("""SELECT * FROM test_table""")

## fetchone获取一行内容
##打印test_table中的第一行
print(c.fetchone())
##打印test_table中的第二行
print(c.fetchone())
##可以用循环语句把这个数据空的每一行都打印出来
##rowcount属性记录了数据库的行数
#for x in range(c.rowcount):
#    print(c.fetchone())

##fetchmany语句返回的是一个元祖
##里面的每个元素也是元祖，代表一行记录
##可以在括号里定义需要获取多少行数据，在以下例子中是2行
#rows=c.fetchmany(2)
#print(rows)

##fetchall语句返回的是一个元祖，
##里面的每个元素也是元祖，代表一行记录
##返回的是所有的元素
#rows=c.fecthall()
#print(rows)

'''
#######################################################
##第四步，插入数据#####
#######################################################
##执行一个插入数据的sql语句
c.execute(
""" 
insert into test_table (username, ’password‘, realname) 
    values 
    ('byhy5', 'password5', 'baiyueheiyun5'),
    ('byhy6', 'password6', 'baiyueheiyun6'),
    ('byhy7', 'password7', 'baiyueheiyun7')
""")

#c.execute(
#"""
#insert into test_table (username, ’password‘, realname)
#    values
#    ('byhy3', 'password3', 'baiyueheiyun3')
#""")
#c.execute(
#"""
#insert into test_table (username, ’password‘, realname)
#    values
#    ('byhy4', 'password4', 'baiyueheiyun4')
#""")

##插入语句必须加commit
connection.commit()
'''

#######################################################
##第五步，获取数据的索引#####
#######################################################
##sql 语句给test_table中的username定义为搜索用的索引
## create index index_username on test_table (username)

##选择某个索引名为'byhy2'的数据列们
#select * from test_table username='byhy2'

##删除某个索引名为'byhy2'的数据列们
## drop 在sql语句中是删除整个table
#delete * from test_table username='byhy2'

##索引会导致表哥数据操作效率下降，因为索引会占索引内存，每次更新数据索引又得更新一遍
##索引需要谨慎使用

##可以定义唯一索引，可以使得某些数据唯一索引，例如登陆名 unique key（username）/ unique(username) / 定义属性 unique在变量最后/ create unique key on ....


#######################################################
##第六步，外健索引，关系型数据库#####
#######################################################
## example 医药公司订单表

##购买药物的客户的数据，不可更改
#create table med_user (
#    id int NOT NULL auto_increment PRIMARY KEY,
#    username varchar(150) NOT NULL,
#    `password` varchar(128) NOT NULL,
#    real_name varchar(30) NOT NULL
#);

##售出药物的数据，不可更改
#create table medicine(
#    id int not null auto_increment PRIMARY KEY,
#    name varchar(150) not null,
#    description varchar(30) not null
#);

##生成的订单的数据，与前两个表的数据关联
##通过foriegn key
## casacde 表示与前两张表同步更新
## delete restrict表示不可以更改这些外健数据
#create table `med_order` (
#    id int not null auto_increment PRIMARY KEY,
#    name varchar(150) not null,
#    user_id int not null,
#    medicine_id int not null,

#    foreign key (user_id)
#     references med_user(id)
#     on update cascade
#     on delete restrict,

#   foreign key (medicine_id)
#     references medicine(id)
#     on update cascade
#     on delete restrict
#);


#######################################################
##第七步，事物，关系型数据库#####
#######################################################
## transaction, 几个操作打包起来一起执行，成功一起成功，失败一起撤销roll back
## example，图书馆的借阅信息管理系统

##借阅的数据，不可更改
#create table book_user (
#    id int NOT NULL auto_increment PRIMARY KEY,
#    username varchar(150) NOT NULL,
#    `password` varchar(128) NOT NULL,
#    real_name varchar(30) NOT NULL
#);

##借出书的数据，不可更改
#create table book(
#    id int not null auto_increment PRIMARY KEY,
#    name varchar(150) not null,
#    `desc` varchar(128) not null,
#    status int not null
#);

##借阅记录表，同步记录借的人和借的书两种数据
#create table borrow (
#    id int not null auto_increment PRIMARY KEY,
#    user_id int not null,
#   book_id int not null,

#    foreign key (user_id)
#     references book_user(id)
#     on update cascade
#     on delete restrict,

#   foreign key (book_id)
#     references book(id)
#     on update cascade
#     on delete restrict
#);


## 1 创建一个事物 transaction， 例如一次借阅记录
#start transaction;

## 2 更新book表 , id 为888的图书借出去了
#update book set status=1 where id=888;

## 3 更新borrow表
#insert into borrow (user_id, book_id) values (1, 888);

## 4 提交事物，前两部一起更新
#commit;

## 5 撤销事物，以上数据全部删除
#roll back;

