
# coding: utf-8

# In[2]:


value = float(input('Input the value'))
danwei = input('Input the 单位：')
if danwei == 'cm':
    value = value/100
    print(value,'m')
elif danwei == 'm':
    value = value *100
    print (value, 'cm')
else:
   print("Wrong stuff")


# In[5]:


score = int(input('Input the score: '))
if score>=90:
    print('A')
elif score>=80 and score<90:
    print('B')
elif score>=70 and score<80:
    print('C')
elif score>=60 and score<70:
    print('D')
else:
    print("Fail!")


# In[10]:


from random import randint
face = randint(1,6)
if face == 1:
    print("a")
elif face == 2:
    print("b")
elif face == 3:
    print("c")
elif face == 4:
    print("d")
elif face ==5:
    print('e')
else:
    print("f")


# In[14]:


import getpass
username = input('请输入用户名: ')
password = getpass.getpass('请输入口令: ') #这样显示的就是隐码
if username == 'admin' and password == '123456':
	print('身份验证成功!')
else:
	print('身份验证失败!')

