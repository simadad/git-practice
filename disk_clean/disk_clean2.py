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
del_files = re.findall(r'(?<=\.)\w+', del_data)
# 正则环视匹配垃圾文件扩展名


def del_dir_or_file(del_root):
    # 统计并删除文件或空文件夹
    global dir_numb, file_numb, size
    try:
        del_size = os.path.getsize(del_root)
        os.remove(del_root)
        file_numb += 1
        size += del_size
        print 'file: ' + del_root + ' removed'
    except WindowsError:
        try:
            del_size = os.path.getsize(del_root)
            os.rmdir(del_root)
            dir_numb += 1
            size += del_size
            print 'dir: ' + del_root + ' removed'
        except WindowsError:
            pass


def get_dir_size_and_del(temp_dir):
    # 统计并删除非空文件夹
    for gds_root, gds_dirs, gds_files in os.walk(temp_dir, topdown=False):
        # 生成并展开以 root 为根目录的目录树，参数 topdown 设定展开方式从底层到顶层
        for gds_dir in gds_dirs:
            # 统计并删除根目录下所有文件夹（已删空）
            gds_full_path = os.path.join(gds_root, gds_dir)
            # 组合完整路径
            del_dir_or_file(gds_full_path)
        for gds_file in gds_files:
            # 统计并删除根目录下所有文件
            gds_full_path = os.path.join(gds_root, gds_file)
            del_dir_or_file(gds_full_path)
    try:
        del_dir_or_file(temp_dir)
        # 删除根目录
    except WindowsError:
        pass

root_sys_drive = os.environ['systemdrive'] + '\\'
# 获取系统盘
root_user_profile = os.environ['userprofile']
# 获取用户目录
root_win_dir = os.environ['windir']
# 获取 Windows 目录
dir_numb = 0
file_numb = 0
size = 0
# 初始化统计数据
get_dir_size_and_del(os.path.join(root_user_profile, 'cookies'))
get_dir_size_and_del(os.path.join(root_user_profile, 'recent'))
get_dir_size_and_del(os.path.join(root_user_profile, 'Temp'))
get_dir_size_and_del(os.path.join(root_user_profile, 'Temporary Internet Files'))
get_dir_size_and_del(os.path.join(root_win_dir, 'prefetch'))
get_dir_size_and_del(os.path.join(root_win_dir, 'temp'))
# 组合垃圾文件夹完整路径，调用函数统计并删除

for roots, dirs, files in os.walk(root_sys_drive, topdown=False):
    for every_file in files:
        # 遍历、判断并统计、删除所有扩展名符合条件的文件
        try:
            file_extension = re.findall(r'(?<=\.)\w+$', every_file)[0]
            # 逆序肯定环视，匹配每个文件的扩展名
        except IndexError:
            # 排除无扩展名文件正则匹配报错
            file_extension = ''
        if file_extension in del_files:
            full_path = os.path.join(roots, every_file)
            del_dir_or_file(full_path)
print '\nfinished'
print 'cleaned files：', file_numb
print 'cleaned directory：', dir_numb
print 'cleaned total data size：', size, ' bite'
