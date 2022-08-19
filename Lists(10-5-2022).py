Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[1,2,3,4,5]
>>> print(l)
[1, 2, 3, 4, 5]
>>> print(l[0])
1
>>> print(l[:5])
[1, 2, 3, 4, 5]
>>> print(l[-1])
5
>>> l.extend([6,7,8])
>>> print(l)
[1, 2, 3, 4, 5, 6, 7, 8]
>>> len(l)
8
>>> l.extend([9,10])
>>> print(l)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> l[0]=12
>>> print(l)
[12, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> l.append([11,1,14])
>>> print(l)
[12, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 1, 14]]
>>> l[1:3]=[20,30,40]
>>> print(l)
[12, 20, 30, 40, 4, 5, 6, 7, 8, 9, 10, [11, 1, 14]]
>>> l.sort(reverse=true)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    l.sort(reverse=true)
NameError: name 'true' is not defined
>>> l.sort(reverse=True)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    l.sort(reverse=True)
TypeError: '<' not supported between instances of 'int' and 'list'
>>> del[-1]
SyntaxError: can't delete operator
>>> remove([11,1,14])
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    remove([11,1,14])
NameError: name 'remove' is not defined
>>> l.reverse()
>>> print(l)
[[11, 1, 14], 10, 9, 8, 7, 6, 5, 4, 40, 30, 20, 12]
>>> l=[1,2,3]
>>> m=l
>>> print(m)
[1, 2, 3]
>>> l.remove([11,1,14])
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    l.remove([11,1,14])
ValueError: list.remove(x): x not in list
>>> remove(l[-1])
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    remove(l[-1])
NameError: name 'remove' is not defined
>>> print(l)
[1, 2, 3]
>>> l.remove(1)
>>> print(l)
[2, 3]
>>> l.append([10,20,30])
>>> print(l)
[2, 3, [10, 20, 30]]
>>> l.remove([10,20,30])
>>> print(l)
[2, 3]
>>> 
