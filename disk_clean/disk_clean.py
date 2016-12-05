# coding: utf-8
import os
import re

del_dir = r'''
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
del_dirs = re.findall(r'(?<=\\).+(?=\\)', del_dir)
del_files = re.findall(r'(?<=\.)\w+', del_dir)
# 正则环视匹配垃圾文件夹名及垃圾文件扩展名


def get_size_and_del(gsd_root):
    # 删除文化或文件夹，并统计大小与数量
    global file_numb, dir_numb, size
    try:
        # 判断并移除文件
        t_size = os.path.getsize(gsd_root)
        os.remove(gsd_root)
        file_numb += 1
        size += t_size
        print 'file：' + gsd_root + ' cleaned'
    except WindowsError:
        try:
            # 格式不正确则移除文件夹
            t_size = os.path.getsize(gsd_root)
            os.rmdir(gsd_root)
            dir_numb += 1
            size += t_size
            print 'dir：' + gsd_root + ' cleaned'
        except WindowsError:
            pass
            # 文件夹不为空则跳过


root_sys_drive = os.environ['systemdrive'] + '\\'
# 获取系统盘
root_user_profile = os.environ['userprofile']
# 获取用户目录
dir_numb = 0
file_numb = 0
size = 0
# 初始化统计数据
for roots, dirs, files in os.walk(root_sys_drive, topdown=False):
    # 生成并展开以 root 为根目录的目录树，参数 topdown 设定展开方式从底层到顶层
    print 'roots：' + roots
    dir_to_del = re.findall(r'(?<=\\)[^\\]*$', roots)[0]
    # 逆序肯定环视，匹配根目录
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
            # 排除无扩展名文件正则匹配报错
            file_extension = ''
        if dir_to_del in del_dirs and root_user_profile in roots or file_extension in del_files:
            full_path = os.path.join(roots, every_file)
            # 组合文件完整路径
            get_size_and_del(full_path)
            # 调用函数判断、删除并统计文件
print '\nfinished'
print 'cleaned files：', file_numb
print 'cleaned directory：', dir_numb
print 'cleaned total data size：', size, ' bite'
