# -*- coding: utf-8 -*-
import sqlite3
Database = sqlite3.connect('address_book.db')
try:
    Database.execute('''
    create table contact(
    id  int primary key not null,
    name    text        not null,
    phone   int         not null,
    email  text        not null);
    ''')
except sqlite3.OperationalError:
    pass


def insert(data, database=Database, table='contact'):
    # 数据库写入
    database.execute('''
    insert into %s values(%s);
    ''' % (table, data))


def select(data, database=Database, table='contact'):
    # 数据库检出
    return database.execute('''
    select %s from %s;
    ''' % (data, table))


def delete(data, database=Database, table='contact'):
    # 数据库删除
    database.execute('''
    delete from %s where id = %s;
    ''' % (table, data))


def data_in(num):
    print ('*开始录入*')
    name = raw_input('姓名：')
    phone = raw_input('手机：')
    emain = raw_input('邮箱：')
    print ('联系人ID：%s' % num)
    name = '"%s"' % name
    emain = '"%s"' % emain
    info = '%s, %s, %s, %s' % (num, name, phone, emain)
    insert(info)
    print ('*录入成功*\n')


def data_find():
    find = raw_input('查找关键字： ').decode('utf-8')
    data = select('*').fetchall()
    have = False
    print ('ID  姓名    手机     邮箱')
    for i in data:
        for j in range(0, 4):
            if type(i[j]) == unicode:
                if find in i[j]:
                    print ('%d   %s %s %s' % (i[0], i[1].encode('utf-8'), i[2], i[3].encode('utf-8')))
                    have = True
                    break
            else:
                if find in str(i[j]):
                    print ('%d   %s %s %s' % (i[0], i[1].encode('utf-8'), i[2], i[3].encode('utf-8')))
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
        print ('%d   %s %s %s' % (i[0], i[1].encode('utf-8'), i[2], i[3].encode('utf-8')))
    print


def data_del():
    print ('*开始删除*')
    del_numb = raw_input('联系人ID：')
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


# 开始
print ('欢迎使用本通讯录')
ID = 0
while True:
    print ('您可以：1.录入 2.查找 3.全部显示 4.删除 (回车退出)')
    key = raw_input('请选择操作码：')
    if key == str(1):
        ID += 1
        data_in(ID)
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
