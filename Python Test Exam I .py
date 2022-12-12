#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#To get the same numbers next to each other. (without a space between them) you need to make a string
#and then use the multiply operator string concatenation


for i in range(1, 6):
    print(str(i) * 5)


# In[ ]:


x = 1 / 2 + 3 // 3 + 4 ** 2
print(x)


# In[ ]:


#The 0o prefix means that the number after it is denoted as:
#Octal notation


# In[ ]:


#YIELD: The yield statement returns a generator object to the one who calls the function which contains yield, 
#instead of simply returning a value.
#return sends back the value and ends the program, yield doesnt end the program.

def func(data):
    for d in data[::2]:
        yield d
 
for x in func('abcdef'):
    print(x, end='')


# In[ ]:


# Escape values
x = '\''
print(len(x))


# In[ ]:


# x = false, it is empty. SPace counts as a value for y.
w = bool(23)
x = bool('')
y = bool(' ')
z = bool([False])
print (w, x, y, z)


# In[ ]:


#What is the default return value for a function that does not explicitly return any value?
#So, if you don't explicitly use a return value in a return statement, or if you totally 
#omit the return statement, then Python will implicitly return a default value for you. 
#That default return value will always be None .


# In[ ]:


def test(x=1, y=2):
    x = x + y
    y += 1
    print(x, y)
 
test(2, 1)


# In[ ]:


#Short Hand If ... Else
#If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

def func(x):
    return 1 if x % 2 != 0 else 2
 
print(func(func(1)))


# In[ ]:


#2 ways of calling the same function and result.
#Also there are 2 functions to be called. The process is done twice. 

def func(x):
    if x % 2 != 0:
        return 1
    else: 2
 
print(func(func(1)))


# In[ ]:


#Aggregates: List2 feeds from list1, once the latter is changed the former does too. 
#A list is mutable. When you assign it to a different variable, you create a reference of the same object.
#If afterwards you change one of them, the other one is changed too.

list1 = [1, 3]
list2 = list1
list1[0] = 4
print(list2)


# In[ ]:


#They refer to the same list. The objects are of the same lenght. No slicing, just assigning values. 
nums = [1, 2, 3]
vals = nums
del vals[1:2]
print(nums)
print(vals)


# In[ ]:


#
i = 0
while i <= 3:
    i += 2
    print('*')


# In[ ]:


x = [3,1,4,1,5,9]
for i in x:
    print (i)


# In[ ]:


x = [3,1,4,1,5,9]
for index, n in enumerate(x):
    print (index, n)


# In[7]:


#The iteration will happen twice range(num) = range (0, 1, 2) Excluding 2.  
#The return clause ends the function, no item is returned.

def func(num):
    res = '*'
    for _ in range(num):
        res += res
    return res

for x in func(2):
    print(x, end='')


# In[12]:


#The snippet comes from the function, goes to x and y, then function gets called with x and y and their value;
#but going back to the function x and y get reassigned by p1 and p2[0]. X is the same 3 but y[0] is 42 now.
#Finally we print x and y[0]
#It is a big difference, whether you pass a mutable or an immutable data type.

def func(p1, p2):
    p1 = 1
    p2[0] = 42
 
x = 3
y = [1, 2, 3]
 
func(x, y)
 
print(x, y[0])


# In[13]:


print(list('hello'))


# In[14]:


#x.insert(position, element)
x = [0, 1, 2]
x.insert(0, 1)
del x[1]
print(sum(x))


# In[15]:


#If you calculate with a boolean True becomes the integer 1 and therefore 1 + True is 2
a = 1
b = 0
x = a or b
y = not(a and b)
print(x + y)


# In[16]:


a = 1
b = 0
x = a or b
print(x)         # 1
print(1 or 0)    # 1
y = not(a and b)
print(y)         # True
print(1 and 0)   # 0
print(not 0)     # True
print(x + y)     # 2
print(1 + True)  # 2


# In[19]:


123 + 0.0


# In[23]:


x = 2
y = 1
# x *= y + 1
x = x * (y + 1) # = x = x * (y + 1) You must know what to mutiply x for. 
print(x)  # 4


# In[3]:


#A list is a mutable data type. Assigning a mutable data type creates a reference to the same object.
# vals and nums will point to the same object in the memory and when you change one you automatically change 
#the other, too. Same list, same length

nums = [1, 2, 3]
vals = nums
del vals[1:2]
print (nums)
print (vals)


# In[1]:


#What is the expected output of the following code?

data = ['Peter', 404, 3.03, 'Wellert', 33.3]
print(data[1:3])


# In[4]:


#What is the expected output of the following code if the user enters 2 and 4? Strings.
x = input()
y = input()
print(x + y)


# In[6]:


#What is the expected output of the following code?

x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z
print(x, y, z)


# In[7]:


#A variable name shadows into a function. You can use it in an expression like in func2()
#or you can assign a new value to it like in func3() BUT you can not do both at the same time like in func()
#There is going to be the new variable num and you can not use it in an expression before its first assignment.

num = 1
 
def func():
    num = num + 3
    print(num)
 
func()
 
print(num)


# In[8]:


name = 'Alice'


def example():
    # ✅ this is ok
    print(name)


example()  # 👉️ 'Alice'


# In[19]:


#The Python "UnboundLocalError: Local variable referenced before assignment" occurs when we reference a local 
#variable before assigning a value to it in a function. To solve the error, mark the variable as global in the 
#function definition, e.g. global my_var.

name = 'Alice'


def example():
    global name
    # ⛔️ UnboundLocalError: local variable 'name' referenced before assignment
      
    print(name)
    name = 'Bob'

  


example()


# In[44]:


#What is the expected output of the following code?
#This function looks for the highest element in a two dimensional list (or another iterable). In the beginning 
#the first number data[0][0] gets taken as possible result. In the inner for loop every number is compared to the 
#possible result. If one number is higher it becomes the new possible result.And in the end the result is 
#the highest number.

x = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print (x)
print (len(x))
 
def func(data):
    res = data[0][0]
    for da in data:
        for d in da:
            if res < d:
                res = d
    return res
 
print(func(x[0]))


# In[23]:


#The indentation in num is key. Outside of the while loop is an infinite. Inside it it prints trice. 
def func(text, num):
    while num > 0:
        print(text)
        num = num - 1
 
func('Hello', 3)


# In[40]:


#The knowledge you need here is that a dictionary can have indexes of different data types.
d = {}
d[1] = 1
d['1'] = 2

d[1] += 1
print(d)
 
sum = 0
 
for k in d:
    sum += d[k]
 
print(sum)


# In[38]:


#The knowledge you need here is that a dictionary can have indexes of different data types.
d = {}
print(d)  # {}

d[1] = 1
print(d)  # {1: 1}

d['1'] = 2
print(d)  # {1: 1, '1': 2}

d[1] += 1
print(d)  # {1: 2, '1': 2}


# In[ ]:


dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)
 
for x in dct.keys():
    print(dct[x][1], end='')


# In[28]:


#A list is a mutable data type and it is passed by reference to a function. Meaning that the list inside of the 
#function and the list outside of the function will point to the same object in the memory. If you change the 
#list inside of the function that will change the list outside of the function in the same way.

my_list = [1, 2, 3]
 
 
def delete_first(x):
    del x[0]
 
 
delete_first(my_list)
print(my_list)  # [2, 3]


# In[29]:


# Integer is an immutable data type. The values get copied from one variable to another. In the end x 
# and y changed their values.

x = 1
y = 2
z = x
x = y
y = z
print(x, y)


# In[33]:


#The fun() function is defined with any parameters and therefore it cannot be called with an argument.
def fun():
    return True
x = fun(False)
print(x)


# In[ ]:




