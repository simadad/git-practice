# coding: utf-8
import os
import re

del_data = r'''
%SystemDrive%
*.tmp
*._mp
*.log
*.gid
*.chk
*.old
*.xlk
*.bak

%UserProfile%
%windir%\prefetch\*.*
%windir%\temp\*.*
%userprofile%\cookies\*.*
%userprofile%\recent\*.*
%userprofile%\Temporary Internet Files\*.*
%userprofile%\Temp\*.*
'''


def get_size_and_del(gsd_root):
    # 删除文化或文件夹，并统计大小与数量
    global file_numb, dir_numb, size
    try:
        # 判断并移除文件
        t_size = os.path.getsize(gsd_root)
        os.remove(gsd_root)
        file_numb += 1
        size += t_size
        print 'file：' + gsd_root + ' removed'
    except WindowsError:
        try:
            # 格式不正确则移除文件夹
            t_size = os.path.getsize(gsd_root)
            os.rmdir(gsd_root)
            dir_numb += 1
            size += t_size
            print 'dir：' + gsd_root + ' removed'
        except WindowsError:
            pass
            # 文件夹不为空则跳过

dir_numb, file_numb, size = 0, 0, 0
# 初始化统计数据
root_sys_drive = os.environ['systemdrive'] + '\\'
# 获取系统盘
root_user_profile = os.environ['userprofile']
# 获取用户目录
root_win_dir = os.environ['windir']
# 获取 Windows 目录
del_files = re.findall(r'(?<=\.)\w+', del_data)
# 匹配垃圾文件扩展名
temp_del_userprofile = re.findall(r'(?<=%userprofile%\\).+(?=\\)', del_data)
# 获取用户文目录下垃圾文件夹名
del_userprofile = map(lambda temp_dir: os.path.join(root_user_profile, temp_dir), temp_del_userprofile)
# 组合用户文目录下垃圾文件夹全目录名
temp_del_windir = re.findall(r'(?<=%windir%\\).+(?=\\)', del_data)
del_windir = map(lambda temp_dir: os.path.join(root_win_dir, temp_dir), temp_del_windir)

for roots, dirs, files in os.walk(root_sys_drive, topdown=False):
    # 生成并展开以 root 为根目录的目录树，参数 topdown 设定展开方式从底层到顶层
    for every_dir in dirs:
        full_path = os.path.join(roots, every_dir)
        # 组合文件夹完整路径
        get_size_and_del(full_path)
        # 调用函数判断、删除并统计空文件夹
    for every_file in files:
        try:
            file_extension = re.findall(r'(?<=\.)\w+$', every_file)[0]
            # 逆序肯定环视，匹配每个文件的扩展名
        except IndexError:
            # 排除无扩展名文件正则匹配时报错
            file_extension = ''
        condition = False
        for i in range(len(del_userprofile)):
            condition += del_userprofile[i] in roots
        for i in range(len(del_windir)):
            condition += del_windir[i] in roots
        condition += file_extension in del_files
        # 组合判断条件
        if condition:
            full_path = os.path.join(roots, every_file)
            # 组合文件完整路径
            get_size_and_del(full_path)
            # 调用函数判断、删除并统计文件
print '\nfinished'
print 'cleaned files：', file_numb
print 'cleaned directory：', dir_numb
print 'cleaned total data size：', size, ' bite'
