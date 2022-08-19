Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> str="Nafisa"
>>> print(str)
Nafisa
>>> str="data science with python"
>>> str.capitalize()
'Data science with python'
>>> str="Nafisa is avery very good girl"
>>> str.count("very")
2
>>> str="Nafisa"
>>> str.isalpha()
True
>>> str="Nafisa kousar"
>>> str.isalpha()
False
>>> str="Nafisa"
>>> str.isdigit()
False
>>> str="12 34"
>>> str.isdigit()
False
>>> str="1234"
>>> str.isdigit()
True
>>> str="RABBANI"
>>> str.isupper()
True
>>> str="NaZEER"
>>> str.isupper()
False
>>> str="rasool bi"
>>> str.islower()
True
>>> str="Nafisa"
>>> str.islower()
False
>>> str="Data Science"
>>> str.isspace()
False
>>> str=" "
>>> str.isspace()
True
>>> str="Python Is Good"
>>> str.istitle()
True
>>> str="PYTHON"
>>> str.istitle()
False
>>> str="Nafisa is a good girl"
>>> str.upper()
'NAFISA IS A GOOD GIRL'
>>> str="NAfisa Is A Good Girl"
>>> str.lower()
'nafisa is a good girl'
>>> str="IT is good Language"
>>> str.partition('is')
('IT ', 'is', ' good Language')
>>> s1="abc"
>>> s2="123"
>>> s1.join(s2)
'1abc2abc3'
>>> str="I am a good girl"
>>> str.replace("boy","girl")
'I am a good girl'
>>> str="i love my india"
>>> str.split()
['i', 'love', 'my', 'india']
>>> str="my NAmE Is Nafisa"
>>> str.swapcase()
'MY naMe iS nAFISA'
>>> str="NAFISA"
>>> len(str)
6
>>> str="rabbani"
>>> len(str)
7
>>> str="Rabbani"
>>> max(str)
'n'
>>> str="NAfisa"
>>> max(str)
's'
>>> str="NAFISA"
>>> min(str)
'A'
>>> str="technology123"
>>> str.isalnum()
True
>>> str="technology"
>>> str.isalnum()
True
>>> str="1234"
>>> str.isalnum()
True
>>> str="tech 123"
>>> str.isalnum()
False
>>> str="Nafisa IS a CSE student"
>>> str.find("CSE")
12
>>> str="INformation Technology"
>>> str.strip()
'INformation Technology'
>>> str.strip("Technology")
'INformation '



