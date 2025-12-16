#!/usr/bin/env python
# coding: utf-8

# # Ecommerce Purchases Analysis
# 
# In this Exercise you will be given some Fake Data about some purchases done through Amazon! Just go ahead and follow the directions and try your best to answer the questions and complete the tasks. Most of the tasks can be solved in different ways. For the most part, the questions get progressively harder.
# 
# Please excuse anything that doesn't make "Real-World" sense in the dataframe, all the data is fake and made-up.
# 
# Also note that all of these questions can be answered with one line of code.
# 
# **Import pandas and read in the Ecommerce Purchases csv file and set it to a DataFrame called ecom.**

# 'Ecommerce Purchases.csv'

# In[1]:


import numpy as np
import pandas as pd
df=pd.read_csv('Ecommerce Purchases.csv')
ecom=pd.DataFrame(df)
ecom


# **Check the head of the DataFrame.**

# In[2]:


ecom.head()


# **How many rows and columns are there?**

# In[4]:


ecom.shape


# **What is the average Purchase Price?**

# In[7]:


avg_purchase=ecom['Purchase Price'].mean()
avg_purchase


# **What were the highest and lowest purchase prices?**

# In[8]:


high_prices=ecom["Purchase Price"].max()
high_prices


# In[9]:


low_prices=ecom["Purchase Price"].min()
low_prices


# **How many people have English 'en' as their Language of choice on the website?**

# In[10]:


ecom.loc[ecom["Language"]=="en"].shape[0]


# **How many people have the job title of "Lawyer" ?**
# 

# In[11]:


ecom.loc[ecom["Job"]=="Lawyer"].shape[0]


# **How many people made the purchase during the AM and how many people made the purchase during PM ?**
# 
# **(Hint: Check out [value_counts()]**

# In[13]:


ecom["AM or PM"].value_counts()


# In[ ]:





# In[ ]:





# **What are the 5 most common Job Titles?**

# In[14]:


ecom["Job"].value_counts().head(5)


# **Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction?**

# In[15]:


ecom.loc[ecom["Lot"]=="90 WT","Purchase Price"]


# In[ ]:





# **What is the email of the person with the following Credit Card Number: 4926535242672853**

# In[16]:


ecom.loc[ecom["Credit Card"]==4926535242672853,"Email"]


# **How many people have American Express as their Credit Card Provider *and* made a purchase above $95 ?**

# In[17]:


ecom[(ecom["CC Provider"]== "American Express")& (ecom["Purchase Price"] > 95)] .shape[0]


# In[ ]:





# In[ ]:





# In[ ]:





# **Hard: How many people have a credit card that expires in 2025?**

# In[18]:


ecom["CC Exp Date"].str.endswith("/25").shape[0]


# In[ ]:





# **Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)** 

# In[20]:


ecom['Email Provider'] = ecom['Email'].str.split('@').str[1]
ecom['Email Provider'].value_counts().head(5)


# # Great Job!
