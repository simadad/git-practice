# -*- coding: utf-8 -*-
import sqlite3
import re
import my_func
Database = sqlite3.connect('address_book.db')
try:
    Database.execute('''
    create table contact(
    id  int primary key,
    name    text        not null,
    phone   int         not null,
    email  text        not null);
    ''')
except sqlite3.OperationalError:
    pass


def insert(data, database=Database, table='contact'):
    # 数据库写入
    database.execute('''
    insert into %s values(null, %s);
    ''' % (table, data))
    database.commit()


def select(data, database=Database, table='contact', condition=None):
    # 数据库检出
    if condition:
        return database.execute('''
            select %s from %s where %s;
            ''' % (data, table, condition))
    else:
        return database.execute('''
                select %s from %s;
                ''' % (data, table))


def delete(data, database=Database, table='contact'):
    # 数据库删除
    database.execute('''
    delete from %s where id = %s;
    ''' % (table, data))
    database.commit()


def data_in():
    print ('*开始录入*')
    name = raw_input('姓名：')
    phone = my_func.numb('手机：')
    while True:
        if re.match(r'1[0-9]{10}', str(phone)):
            break
        else:
            phone = my_func.numb('格式错误,请重新输入：')
    emain = raw_input('邮箱：')
    while True:
        if re.match(r'\w{1,20}@\w{1,10}\.\w{1,5}', emain):
            break
        else:
            emain = raw_input('格式错误,请重新输入：')
    name = '"%s"' % name
    emain = '"%s"' % emain
    info = '%s, %s, %s' % (name, phone, emain)
    insert(info)
    print ('*录入成功*\n')


def prints(data):
    print ('%d   %s %s %s' % (data[0], data[1].encode('utf-8'), data[2], data[3].encode('utf-8')))


def data_find():
    find = raw_input('查找关键字： ').decode('utf-8')
    data = select('*').fetchall()
    have = False
    print ('ID  姓名    手机     邮箱')
    for i in data:
        for j in range(0, 4):
            if type(i[j]) == unicode:
                if find in i[j]:
                    prints(i)
                    have = True
                    break
            else:
                if find in str(i[j]):
                    prints(i)
                    have = True
                    break
    if have:
        pass
    else:
        print ('查询无果')
    print


def data_show():
    data = select('*').fetchall()
    print ('ID  姓名    手机     邮箱')
    for i in data:
        prints(i)
    print


def data_del():
    print ('*开始删除*')
    del_numb = my_func.numb('联系人ID：')
    conditions = 'id == %s' % del_numb
    to_del = select('*', condition=conditions).fetchall()
    if to_del:
        for i in to_del:
            prints(i)
        while True:
            confirm = raw_input('确定删除此联系人？（Y/N） ：').decode('utf-8')
            if confirm == u'Y':
                delete(del_numb)
                print ('成功删除\n')
                break
            elif confirm == u'N':
                print ('取消删除\n')
                break
            else:
                print ('输入“Y”确认删除，输入“N”取消删除！')
                continue
    else:
        print ('无此ID')

# 开始
print ('欢迎使用本通讯录')
while True:
    print ('您可以：1.录入 2.查找 3.全部显示 4.删除 (回车退出)')
    key = raw_input('请选择操作码：')
    if key == str(1):
        data_in()
    elif key == str(2):
        data_find()
    elif key == str(3):
        data_show()
    elif key == str(4):
        data_del()
    else:
        Database.commit()
        Database.close()
        break
