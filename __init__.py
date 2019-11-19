# -*- coding: utf-8 -*-
_author_ = 'luwt'
_date_ = '2018/7/23 10:37'


"""
需要安装pdfkit，另外需要安装可执行文件wkhtmltopdf.exe，
pdfkit核心命令是调用wkhtmltopdf.exe实现转pdf
有三个接口：
pdfkit.from_url
pdfkit.from_string
pdfkit.from_file
需要用pdfkit.configuration(wkhtmltopdf=path_wk)来说明wkhtmltopdf.exe的安装位置，否则会找不到
options来约定纸张大小，属性'encoding'约定编码，以防乱码
"""
