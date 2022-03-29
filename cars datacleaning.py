#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[9]:


cars=pd.read_csv("Cars.csv")
cars.info()


# In[13]:


df=pd.read_csv("Cars.csv")
df


# In[18]:


df.columns


# In[20]:


df.dtypes


# In[23]:


df["MPG"]=round(df["MPG"],2)
df


# In[27]:


df["SP"]=round(df["SP"],2)
df


# In[30]:


df["WT"]=round(df["WT"],0)
df


# In[42]:


df["HP"]=df["HP"].astype(float)
df.dtypes


# In[46]:


df["VOL"]=df["VOL"].astype(float)
df.dtypes


# In[48]:


df.isnull().sum()


# In[54]:


df["HP"]=round(df["HP"],2)
df


# In[56]:


df.HP


# In[58]:


df.MPG


# In[60]:


df.SP


# In[65]:


df.VOL


# In[64]:


df.columns


# In[67]:


df.WT


# In[69]:


df["SP"].unique


# In[71]:


df["HP"].unique


# In[74]:


df.describe()


# In[77]:


missing=df[df.isnull().any(axis=1)]
missing


# In[96]:


df=pd.read_csv("Cars.csv")
df1=pd.read_csv("Cars.csv",index_col=0,usecols=["HP","MPG","VOL","SP","WT"])
df1


# In[101]:


plt.scatter(df1["VOL"],df1["SP"],c="red")


# In[117]:


plt.scatter(df["VOL"],df["SP"],c="blue")
plt.xlabel("VOL")
plt.ylabel("SP")


plt.show


# In[151]:


plt.hist(df["HP"],color="blue",edgecolor="white",orientation="vertical",bins=5)
plt.xlabel=("frequency")
plt.ylabel=("HP")
plt.show


# In[157]:


pip install seaborn


# In[161]:


import seaborn as sns


# In[166]:


sns.set(style="darkgrid")
sns.regplot(x=df["HP"],y=df["SP"])


# In[169]:


sns.regplot(x=df["HP"],y=df["SP"],fit_reg=False)#fit_reg=False removes the regresssion line from plot


# In[178]:


sns.regplot(x=df["HP"],y=df["SP"],marker="*",fit_reg=False)#marker="*" is used to change the shape of the pointers


# In[ ]:




