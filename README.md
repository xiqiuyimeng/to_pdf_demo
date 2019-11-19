# to_pdf_demo
The demo which is able to convert str or file to pdf.
On my pc, it's windwos OS system, so pdfkit must install the dependency `wkhtmltopdf.exe` which provide ablility to convert a str or a file which like `html` to the file of pdf format. 
And a file not like `html` will be deal with win32com module, to attention, if com interface used is wps official version, the dispatchEx should be `wps.Application`, or it should be `kwps.Application`, else if com interface used is Microsft word interface, create object should be `word.Application`.
