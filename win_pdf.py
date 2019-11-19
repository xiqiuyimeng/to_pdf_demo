# -*- coding: utf-8 -*-
import comtypes.client as ct
from win32com import client

_author_ = 'luwt'
_date_ = '2019/2/22 14:22'


class FileToPdf:

    def doc_to_pdf(self, f, pdf):
        # 由于是wps试用版，所以是kwps，否则应该为wps，或者使用comtypes的client关键词为word
        word = client.DispatchEx('kwps.Application')
        doc = word.Documents.Open(f)
        doc.SaveAs(pdf, FileFormat=17)
        doc.Close()
        word.Quit()


# FileToPdf().doc_to_pdf('D:\\数据词典demo.doc', 'D:\\数据词典demo.pdf')
