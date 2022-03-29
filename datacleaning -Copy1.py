#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
iris1= pd.read_csv("iris.csv")
df=iris1
df1=df.copy(deep=True)
df1


# In[12]:


df.memory_usage(deep=True)


# In[15]:


df.loc[:,'Species']


# In[23]:


df.loc[:,'Sepal.Length']


# In[25]:


df.select_dtypes(exclude=[object])


# In[27]:


df.select_dtypes(include=[object])


# In[29]:


df


# In[32]:


df.info()


# In[35]:


df.Species.unique


# In[38]:


df.columns


# In[41]:


import numpy as np


# In[43]:



np.unique(df['Sepal.Length'])


# In[45]:


np.unique(df['Species'])


# In[49]:


df.select_dtypes(exclude=[index])


# In[53]:


df2=pd.read_csv("iris.csv",na_values=("??","###"))
df2


# In[68]:


df['Sepal.Length',]=df['Sepal.Length'].astype("int64")
np.unique(df['Sepal.Length'])
df.dtypes#converting of FLoat datatypes int integer


# In[75]:


df['Sepal.Width']=df['Sepal.Width'].astype("int64")
np.unique(df['Sepal.Width'])
df.dtypes#converting of FLoat datatypes int integer


# In[87]:


df['Sepal.Length',]=df['Sepal.Length'].astype("float64")
np.unique(df['Sepal.Length'])
df.dtypes#converting of int datatypes float


# In[90]:


df.dtypes


# In[92]:


df.loc[:,'Sepal.Length']


# In[94]:


df['Sepal.Length'].unique


# In[97]:


#TO check null values
df.isnull().sum()


# In[106]:


df['Species'].replace("setosa",1,inplace=True)
df.Species
#if we want to replace the values of string with int example"four replaced with 4"


# In[125]:


df.insert(5,"Sepal_coverted",0)


# In[129]:


df.columns


# In[132]:


df.head()


# In[146]:


df["Petal.Length"]=round(df["Petal.Length"],2)#to convert data into less decimal points 
df


# In[147]:


df


# In[152]:


#to find the missing values in all the rows
missing=iris1[iris1.isnull().any(axis=1)]
missing


# In[156]:


df.describe()


# In[158]:


#to find the "Mean" of the particular coloum
iris1["Sepal.Width"].mean()


# In[162]:


#to replace the missing values with mean value in particular column 
df['Sepal.Width'].fillna(df['Sepal.Width'].mean(),inplace=True)
df


# In[167]:


df["Species"].value_counts()
# for textual data if we want to see the data category wise


# In[181]:


df["Species"].fillna(df["Species"].value_counts().index[0],inplace=True)
df.info()


# In[183]:


df.Species


# In[185]:


df.isnull().sum()


# In[ ]:




