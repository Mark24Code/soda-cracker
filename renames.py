"""
批量更改当前目录下文件名的后缀名
"""
import os

new_extension = '.mp4'

work_dir = os.getcwd()
script_name = __file__.split('/')[-1]

files_list = os.listdir(work_dir)
files_list.remove(script_name)

for filename in files_list:
    short_name, extension = filename.split('.')

    old_abs_file_name = work_dir + os.sep + filename
    new_abs_file_name = work_dir + os.sep + short_name + new_extension

    os.rename(old_abs_file_name, new_abs_file_name)
