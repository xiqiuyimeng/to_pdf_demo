# -*- coding: utf-8 -*-
import pdfkit
_author_ = 'luwt'
_date_ = '2019/4/19 16:25'


class Pdf:

    @staticmethod
    def write_pdf(content, file_name):
        path_wk = 'wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wk)
        # 用options来约定编码格式，以防乱码
        options = {
            'encoding': 'utf-8'
        }
        # with open('D:\\a.docx', 'w', encoding='utf-8')as f:
        #     f.write("数据词典demo")
        # 两种方式，一是先生成文档，通过读取文档生成pdf，二是直接用读取的字符串生成pdf
        # pdfkit是根据html转pdf，所以文件也应当是纯文本文件或者html标签文件，其他文件不适用。
        # with open('D:\\a.docx', 'r', encoding='utf-8')as f:
        #     pdfkit.from_file(f, file_name, configuration=config, options=options)
        pdfkit.from_string(content, file_name, configuration=config, options=options)


# Pdf.write_pdf("This is the first line.<br/>And this is the second line.", "D:\\test.pdf")
