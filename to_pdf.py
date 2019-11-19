# -*- coding: utf-8 -*-
from pdf.win_pdf import FileToPdf
from pdf.generate_pdf import Pdf
import time
import os
_author_ = 'luwt'
_date_ = '2019/4/19 16:55'


def get_file_name(path, ix=None):
    if ix is None:
        ix = 1
    new_name = os.path.join(path, 'test{}.pdf'.format(ix))
    while os.path.exists(new_name):
        ix = ix + 1
        new_name = os.path.join(path, 'test{}.pdf'.format(ix))
    return new_name


user_input = input("请输入要转换的文档路径或要写入pdf文件的字符串")
try:
    # 当前目录的绝对目录
    abs_path = os.path.abspath('.')
    out_path = os.path.join(abs_path, "输出目录")
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    out_file = get_file_name(out_path)
    if os.path.isfile(user_input):
        path_choice = input('输出文件路径选择：是否用原文件路径？ y/n （如果不启用原路径将使用系统默认路径）')
        if path_choice == 'y':
            out_path = os.path.split(user_input)[0]
        name_choice = input('输出文件名称选择：是否用原文件名称？ y/n（如果不启用原名称将使用系统生成）')
        if name_choice == 'y':
            original_name = os.path.splitext(os.path.split(user_input)[1])[0]
            out_file = os.path.join(out_path, '{}.pdf'.format(original_name))
        print("正在执行，请稍后！输出路径为：{}".format(out_file))
        FileToPdf().doc_to_pdf(user_input, out_file)
        print("执行成功！两秒后退出")
        time.sleep(3)
    else:
        print("系统检测输入为非法路径，将直接将输入写入pdf，输出路径为：{}，三秒后执行!".format(out_file))
        time.sleep(3)
        Pdf().write_pdf(user_input, out_file)
        print("执行成功！两秒后退出")
        time.sleep(3)
except Exception as e:
    print("出错了:{}".format(e))



