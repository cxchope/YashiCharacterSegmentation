#coding=utf-8
import sys
import os
import codecs
os.system('clear')
print "=============================="
print "雅詩文本分割器(", sys.argv[0], ")準備進行字符分割"
chrlen = 0
chrlen = int(sys.argv[1])
print "分割字數：", chrlen
infile = ""
infile = sys.argv[2]
print "原文件：", infile
print "=============================="
filecharlen = 0
all_the_text = ""
try:
    file_object = open(infile)
except:
    print "文件讀入失敗，請檢查路徑是否正確或是否包含空格等特殊字符。"
else:
    try:
        all_the_text = file_object.read( )
    finally:
        if all_the_text[:3] == codecs.BOM_UTF8:
            all_the_text = all_the_text[:3]
            all_the_text = all_the_text.decode("utf-8")
        all_the_text = unicode(all_the_text, "utf-8")
        file_object.close( )
        filecharlen = len(all_the_text)
        print "文件已讀入，字符數量：", filecharlen
print "=============================="

#filecharArr = list(all_the_text)
saveChar = []
fileid = 0
for i in range(0, filecharlen):
    nowchar = all_the_text[i]
    saveChar.append(nowchar)
    #print len(saveChar), chrlen
    if len(saveChar) == chrlen or i == filecharlen-1:
        fileid = fileid + 1
        saveFileName = "分割後的文檔%d.txt" %fileid
        #saveFileName = ",".join(saveFileName)
        okText = "".join(saveChar)
        print "正在保存文本文檔“", saveFileName, "” ..."
        ok = okText.encode("utf-8")
        print ok
        fh = open(saveFileName, 'w')
        fh.write(ok)
        fh.close()
        print "已保存文本文檔“", saveFileName, "”。"
        print "------------------------------"
        saveChar = []
print "=============================="
print "雅詩文本分割器完成。"
print "文本編碼：UTF-8"
print "原文件：", infile
print "處理文字數量：", filecharlen
print "分割字數：", chrlen
print "分割為文件數量：", fileid, "(*.txt)"
print "=============================="
#else:
#print "FALSE"
