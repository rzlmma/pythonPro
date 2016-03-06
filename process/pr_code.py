# -*- coding:utf-8 -*-
import subprocess
import os,sys

# os.system('mkdir a')
def test_process():
    try:
        pro = subprocess.Popen(['mkdir', 'b'], stdout=subprocess.PIPE)
    except Exception as e:
        print"Error:", e
    else:
        content = pro.communicate()[0]
        print '\tstdout:',repr(content)

# #管道连接
def muti_process():
    cat = subprocess.Popen(['cat', 'index.rse'], stdout=subprocess.PIPE)

    grep = subprocess.Popen(['grep', '.. include::'], stdin=cat.stdout, stdout=subprocess.PIPE)

    cut = subprocess.Popen(['cut','-f','3', '-d'], stdin=grep.stdout, stdout=subprocess.PIPE)

    for line in cut.stdout:
        print line


def test_sys():
    sys.stderr.write('pr.py: starting')
    sys.stderr.flush()
    while True:
        next_line = sys.stdin.readline()
        if not next_line:
            break
        sys.stdout.write(next_line)
        sys.stdout.flush()
    sys.stderr.write('pr.py: ending')
    sys.stdout.flush()


def test_subprocess():
    pro = subprocess.Popen('repeater.py',
                           # shell=True,
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE
                           )
    for i in range(0,5):
        pro.stdin.write('%d\n'% i)
        output = pro.stdout.readline()
        print output
    remainder = pro.communicate()[0]
    print remainder

if __name__ == '__main__':
    # test_sys()
    test_subprocess()

