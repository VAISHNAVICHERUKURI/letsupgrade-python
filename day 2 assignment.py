Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  #1.LIST AND ITS DEFAULT FUNCTIONS
>>> 
>>> lst=[10,20,30,5,15]
>>> lst
[10, 20, 30, 5, 15]
>>> len(lst)
5
>>> min(lst)
5
>>> lst1=[2,4,6,8]
>>> lst2=[1,3,5,7]
>>> c=(lst1,lst2)
>>> c
([2, 4, 6, 8], [1, 3, 5, 7])
>>> sum(lst1)
20
>>> sum(lst2)
16
>>> 
>>> 
>>> #2.DICTIONARY AND ITS DEFAULT FUNTIONS
>>> 
>>> dit={"name":"vaishnavi","age":20,"number":12345}
>>> dit1={"name":"abcd","age":21,"number":78901}
>>> len(dit)
3
>>> str(dit)
"{'name': 'vaishnavi', 'age': 20, 'number': 12345}"
>>> type(dit)
<class 'dict'>
>>> 
>>> #3.SETS AND ITS DEFAULT VALUES
>>> 
>>> st={"xyz",1,2,2,3,4,4,7,5,6,6}
>>> st
{1, 2, 3, 4, 5, 6, 7, 'xyz'}
>>> st.add(10)
>>> st
{1, 2, 3, 4, 5, 6, 7, 'xyz', 10}
>>> st.discard(4)
>>> print(st)
{1, 2, 3, 5, 6, 7, 'xyz', 10}
>>> a={1,2,3}
>>> b={4,5,6}
>>> print(a|b)
{1, 2, 3, 4, 5, 6}
>>> print(a-b)
{1, 2, 3}
>>> 
>>> 
>>> #4.TUPLE AND ITS DEFAULT FUNCTIONS
>>> 
>>> tup=("sai","@","letsupgrade.in")
>>> tup.count("@")
1
>>> tup1=("abc","@","python")
>>> len(tup)
3
>>> max(tup)
'sai'
>>> min(tup)
'@'
>>> max(tup1)
'python'
>>> 
>>> #5.STRING AND ITS METHODS
>>> 
>>> str=("ab","cd","ef","gh")
>>> str
('ab', 'cd', 'ef', 'gh')
>>> str.count("ef")
1
>>> str.index("cd")
1
>>> str.remove("gh")
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    str.remove("gh")
AttributeError: 'tuple' object has no attribute 'remove'
>>> str.discard("gh")
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    str.discard("gh")
AttributeError: 'tuple' object has no attribute 'discard'
>>> 