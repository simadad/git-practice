# coding: utf-8
import os
import re

del_dir = r'''
*.tmp
*._mp
*.log
*.gid
*.chk
*.old
*.xlk
*.bak

\prefetch\*.*
\temp\*.*
\cookies\*.*
\recent\*.*
\Temporary Internet Files\*.*
\Temp\*.*
\recent\*.*
'''


def get_root(disk_root):
    os.chdir(r'%s://' % disk_root)
    # 改变当前路径到指定目录
    return os.getcwd()
    # 得到当前目录


def get_size_and_del(non_empty_dir):
    ned_size = 0
    for ned_roots, ned_dirs, ned_files in os.walk(non_empty_dir, topdown=False):
        # 逐层遍历当前主根目录下的次根目录、目录下文件夹、目录下文件
        for ned_file in ned_files:
            ned_full_path = os.path.join(ned_roots, ned_file)
            # 组合路径
            ned_size += os.path.getsize(ned_full_path)
            # 得到对应文件的大小或文件夹路径大小 4096 bite
            os.remove(ned_full_path)
            # 移除文件
        for ned_dir in ned_dirs:
            ned_full_path = os.path.join(ned_roots, ned_dir)
            ned_size += os.path.getsize(ned_full_path)
            os.rmdir(ned_full_path)
            # 移除文件夹
    ned_size += os.path.getsize(non_empty_dir)
    os.rmdir(non_empty_dir)
    return ned_size


disk = raw_input('press the disk root to be cleaned\n')
root = get_root(disk)
del_dirs = re.findall(r'(?<=\\).+(?=\\)', del_dir)
del_files = re.findall(r'(?<=\.)\w+', del_dir)
dir_numb = 0
file_numb = 0
size = 0
for roots, dirs, files in os.walk(root, topdown=False):
    # 逐层遍历当前主根目录下的次根目录、目录下文件夹、目录下文件
    try:
        for every_file in files:
            file_extension = re.findall(r'(?<=\.)\w+', every_file)
            if file_extension:
                if file_extension[0] in del_files:
                    full_path = os.path.join(roots, every_file)
                    # 组合根目录及文件名，得到完全路径
                    file_numb += 1
                    size += os.path.getsize(full_path)
                    # 累积文件清理大小
                    os.remove(full_path)
                    # 移除文件
                    print full_path + ' cleaned'
        for every_dir in dirs:
            full_path = os.path.join(roots, every_dir)
            if every_dir in del_dirs:
                dir_numb += 1
                size += get_size_and_del(full_path)
                print full_path + ' cleaned'
            else:
                try:
                    os.rmdir(full_path)
                    dir_numb += 1
                    size += os.path.getsize(full_path)
                except WindowsError:
                    # 不能删除的文件则跳过
                    pass
        print '%s cleaned.' % roots
    except WindowsError:
        pass

print '\nfinished'
print 'cleaned files:', file_numb
print 'cleaned directory:', dir_numb
print 'cleaned total data size:', size, 'bite'
