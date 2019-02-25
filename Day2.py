
# coding: utf-8

# In[2]:


year = int (input('Put in the number of the year: '))
is_year = (year % 4 == 0 and year % 100!=0 or year%400 == 0)
print(is_year)


# In[5]:


c_degree = float(input('Input the celsius degree:   '))
f_degree = 1.8 * c_degree + 32
print(f_degree)


# # 

# In[12]:


import math
radius = float(input('Input the radius:   '))
zhouchang = 2*math.pi*radius
area = math.pi * radius *radius
print ('周长:%.3f'%zhouchang)


# In[15]:


f_degree = float(input('Input 华氏度：'))
c_degree = (f_degree-32)/1.8
print('%.1f华氏度 = %.1f摄氏度' % (f_degree,c_degree))

