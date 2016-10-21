# -*- coding: utf-8 -*-
import sqlite3
def numb(prompt_input=None, prompt_print='Numbers please'):
    # 确保输入为数字
    while True:
        try:
            n = input(prompt_input)
            return n
        except NameError:
            if prompt_input:
                pass
            else:
                print (prompt_print)
            continue
        except SyntaxError:
            if prompt_input:
                pass
            else:
                print (prompt_print)
            continue


def loop(condition, loop_func, tip=None):         # #######  待修改  ##################
    while True:
        if condition:
            return loop_func
        else:
            loop_func
            print (tip)


def new_database(db_name='database.db', tb_name='table_name', tb_content='id  integer primary key,'):
    # 新建或打开数据库表格
    new_db = sqlite3.connect(db_name)
    try:
        new_db.execute('create table %s(%s);' % (tb_name, tb_content))
    except sqlite3.OperationalError:
       pass
    return new_db


def insert(database, table, data):
    # 数据库写入
    database.execute('insert into %s values(null, %s);' % (table, data))
    database.commit()


def select(database, table, key='*', condition=None):
    # 数据库检出
    return database.execute('select %s from %s %s;' % (key, table, condition))


def update(database, table, column, data, condition=''):
    # 数据更新
    database.execute('update %s set %s = %s %s' % (table, column, data, condition))
    database.commit()


def delete(database, table, data):                # 待修改###############################
    # 数据库删除
    database.execute('''
    delete from %s where id = %s;
    ''' % (table, data))
    database.commit()

