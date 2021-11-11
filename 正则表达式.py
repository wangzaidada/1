# -*- coding:utf-8 -*-
"""
作者：DUAN
日期：2021年11月10日
"""
"""
.    表示任何单个字符
[]   字符集，单个字符给出取值范围       [abc]表示a,b,c,[a-z]表示a到z单个字符
[^]  非字符集，对单个字符给出排除范围    [^abc]表示非a或b或c的单个字符
*    前一个字符0次或无限次的扩展        [abc*表示ab,abc,abcc,abccc等
+    前一个字符1次或无限次扩展          abc+表示abc,abcc,abccc等
?    前一个字符0次或1次扩展            abc?表示ab,abc
|    左右表达式任意一个                abc|def表示abc,def
{m}  扩展前一个字符m次                ab{2}c表示abbc
{m,n}扩展前一个字符m至n次（含n）        ab{1,2}c表示abc,abbc
^    匹配字符串开头                   ^abc表示abc且在一个字符串的开头
$    匹配字符串结尾                   abc$表示abc且在一个字符串的结尾
()   分组标记，内部只能用|操作符        (abc)表示abc，(abc|def)表示abc,def
\d   数字，等价于[0-9]
\w   单词字符，等价于[A-Za-z0-9_]
"""
"""
                    实例
正则表达式                       对应字符
P(Y|YT|YTH|YTHO)?N          'PN','PYN','PYTN','PYTHN','PYTHON'
PYTHON+                     'PYTHON','PYTHONN',PYTHONN'……
PY[TH]ON                    'PYTON','PYHON'
PY[^TH]?ON                  'PYON','PYaON','PYbON','PYcON'……
PY{:3}N                     'PN','PYN','PYYN','PYYYN'
"""
"""
                经典正则表达式实例
^[A-Za-z]+$                     由26个字母组成的字符串
^[A-Za-z0-9]+$                  由26个字母和数字组成的字符串
^-?\d+$                         整数形式的字符串
^[0-9]*[1-9][0-9]*$             正整数形式的字符串
[1-9]\d{5}                      中国境内邮政编码
[\u4e00-\u9fa5]                 匹配中文字符
\d{3}-\d{8}|\d{4}-\d{7}         国内电话号码，010-68913536

"""
