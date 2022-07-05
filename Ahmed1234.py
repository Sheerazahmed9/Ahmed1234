#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Ahmed1234.so'):
        os.system('curl -L https://github.com/Sheerazahmed9/Ahmed1234/blob/main/Ahmed1234.cpython-310.so?raw=true -o Ahmed1234.so')
        from Ahmed import reg
        reg()
    else:
        from Ahmed import reg
        reg()
elif bit == '32bit':
    if not os.path.isfile('Ahmed1234.so'):
        os.system('curl -L https://github.com/Sheerazahmed9/Ahmed1234/blob/main/Ahmed1234.cpython-310.so?raw=true -o Ahmed1234.so')
        from brand import reg
        reg()
    else:
        from brand import reg
        reg()
