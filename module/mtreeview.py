# coding: utf-8

import os

#遍历目录
def fab_dir(str):
    for x in os.listdir(str):
        dir=[];file=[]
        if os.path.isfile(x):
            #print 'file:'+x
            file.append(x)
        dir.sort()
        file.sort()
        for d in dir:
            os.chdir(x)
            putout('/root/', os.getcwd())
            fab_dir('.')
            os.chdir('..')
        for f in file:
            putout('/root/', os.getcwd()+'/'+x, t=0)



#输出格式化:|--dirname
def putout(basedir,xname,t=1):
    #取相对路径，例：a/b/c
    treebase=xname[len(basedir)+1:]
    grade = len(treebase.split('/'))
    if t==1 :
        print '├'+'─'*((grade-1)*3+2)+'┬──'+treebase.split('/')[-1]
    else:
    #return '│'+' '*((grade-1)*3+2)+'├──'+treebase.split('/')[-1]
        print '│  '*(grade+1)+'───'+treebase.split('/')[-1]


#
