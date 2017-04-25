#coding=utf-8
# 中文
import hashlib

time='20170424'
rout='F:\\temporaryFiles\\test\\keygen.txt'
f = open(rout, "w")
for i in range(1,200):
    cam=''+time+bytes(i)
    res = hashlib.sha1(cam).hexdigest()
    res = hashlib.sha1(res).hexdigest()
    f.write('key is :'+res+'\n')
    print '第' + bytes(i) + '个激活码  生成时间是' + time + '  key:' + res
f.close()

