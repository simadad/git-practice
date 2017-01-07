# coding: utf-8
import os
import shutil

del_extension = ['.tmp', '._mp', '.log', '.gid', '.chk', '.old', '.xlk', '.bak']
del_userprofile = ['cookies', 'recent', 'Temporary Internet Files', 'Temp']
del_windir = ['prefetch', 'temp']
# 获取系统盘
root_sys_drive = os.environ['systemdrive'] + '\\'
# 获取用户目录
root_user_profile = os.environ['userprofile']
# 获取 Windows 目录
root_win_dir = os.environ['windir']


def del_dir_or_file(root):
    try:
        if os.path.isfile(root):
            # 删除文件
            os.remove(root)
            print 'file: ' + root + ' removed'
        elif os.path.isdir(root):
            # 删除文件夹
            shutil.rmtree(root)
            print 'directory: ' + root + ' removed'
    except WindowsError:
        print 'failure: ' + root + " can't remove"

for roots, dirs, files in os.walk(root_sys_drive, topdown=False):
    # 生成并展开以 root 为根目录的目录树，参数 topdown 设定展开方式从底层到顶层
    for every_file in files:
        # 获取文件扩展名
        file_extension = os.path.splitext(every_file)[1]
        if file_extension in del_extension:
            # 组合文件完整路径
            full_path = os.path.join(roots, every_file)
            # 调用函数删除文件
            del_dir_or_file(full_path)
for every_dir in del_userprofile:
    # 组合文件夹完整路径
    full_path = os.path.join(root_user_profile, every_dir)
    # 调用函数删除文件夹
    del_dir_or_file(full_path)
for every_dir in del_windir:
    full_path = os.path.join(root_win_dir, every_dir)
    del_dir_or_file(full_path)
print '\nfinished'
