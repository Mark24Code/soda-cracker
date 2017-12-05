import os
import sys
import shutil
import time
from datetime import datetime, timedelta

sys_argv = sys.argv
cwd = os.getcwd()
prefix = "前端开发部-张阳-"
subfix = ".docx"

if len(sys_argv)==2 and sys_argv[1]=='--help':
    help_doc = """
    python3 file_generator.py  <参数配置>
    
    用于生成工作日范围的文件
    
    文件名组成： [前缀]日期格式(%Y%m%d)[后缀]
    
    --source    <模板文件> 模板文件文件名
    --forward   <周期数> 向后的周期个数
    --start     <开始日期> 格式(%Y%m%d),例如:20171212
    --prefix    <前缀> 生成文件名
    --subfix    <后缀>
    """
    print(help_doc)
    sys.exit(1)


class ArgError(Exception):
    pass


def getArg(arg_name):
    if arg_name in sys_argv:
        arg_index = sys_argv.index(arg_name)
        if arg_index + 1 > len(sys_argv) + 1:
            raise ArgError('PLZ check args.')
        return sys_argv[arg_index + 1]
    else:
        return None


# get args

source_file = getArg('--source')
forward = int(getArg('--forward')) if getArg('--forward') else 0
start_date_str = getArg('--start')
prefix = getArg('--prefix') if getArg('--prefix') else prefix
subfix = getArg('--subfix') if getArg('--subfix') else subfix

source_file_path = os.path.join(cwd, source_file)

# interval distances
start_date = datetime.today()
if start_date_str:
    start_date = time.strptime(start_date_str, '%Y%m%d')
start_week = start_date.weekday()


distances = []
for cycle in range(forward + 1):
    for i in range(5):
        distances.append(cycle * 7 + i)

slice_index = distances.index(start_week)
rest_distances = distances[slice_index - 1:]

# date generators
for day_distance in rest_distances:
    dst_filename = prefix + (start_date + timedelta(days=day_distance)).strftime("%Y%m%d") + subfix
    shutil.copy(source_file, dst_filename)
    print('克隆完成:{}'.format(dst_filename))

print('生成完成')