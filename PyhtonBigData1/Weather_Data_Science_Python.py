#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv(r"X:\python\DS\Weather_Data.csv")


# In[3]:


data.head()


# In[4]:


data.count()


# In[5]:


data["Weather"].value_counts()


# In[ ]:





# In[6]:


data.nunique()


# # Q)Find all the unique values of 'wind speed' column  in the data?

# In[4]:


data.head(2)


# In[5]:


data.nunique()


# In[9]:


data['Wind Speed_km/h'].nunique()


# In[10]:


data['Wind Speed_km/h'].unique()


# ## Find the no of Times where the Weather is Exactly Clear.

# In[17]:


# 1) valuecounts
data.Weather.value_counts()
# data['Weather'].count()


# In[20]:


#  filtering
# data.Weather == 'Clear'
data[data.Weather=='Clear']


# In[4]:


# group by
data.groupby('Weather').get_group('Clear')


# ## find  the no of times when the 'wind speed' is exactly 4km/hr ?

# In[3]:


data.head(2)


# In[5]:


data[data['Wind Speed_km/h']==4] #ans


# ## find out the all null values in the data ? 

# In[7]:


data.isnull().sum()


# In[8]:


# 2nd way
data.notnull().sum()


# ## Rename the col name 'Weather' to the data frame 'weather' ?

# In[13]:


# data.rename(columns= {'Weather': 'Weather condition' }) # changes for temp purpose
data.rename(columns=  {'Weather' : 'Weather Condition'},inplace=True) # changes for permanently


# In[14]:


data.head(2)


# ## What is the mean visiblity?

# In[6]:


data.head(2)


# In[4]:


data.Visibility_km.mean() # ans


# ## what is the standard deviation of 'pressure' in this data? 

# In[ ]:





# In[ ]:





# In[ ]:





# In[3]:


data.Press_kPa.std()


# ## what is the variance of relative humidity in this data?

# In[4]:


data['Rel Hum_%'].var()


# ## Find all instances when snow was recorded? 

# In[7]:


#value_counts
data['Weather'].value_counts()


# In[9]:


# filtring
data[data.Weather=='Snow']


# In[11]:


# str.contains
data[data.Weather.str.contains('Snow')]


# ## Q) Find all the instances when the wind speed is above 24 and visiblity is 25?

# In[3]:


data.head(2)


# In[4]:


data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km']==25)]


# ## What is the mean value of each column against each weather condtion? 

# In[5]:


data.head(2)


# In[7]:


data.groupby('Weather').mean() # groupby methods groups all unique vals of a particular column.


# ## what is the maximum and minimun value of each column against 'weather'?

# In[8]:


data.groupby('Weather').min() # min values


# In[9]:


data.groupby('Weather').max() # max values


# ## Q) show all the records where weather condition id 'fog'?

# In[10]:


data.head(2)


# In[11]:


data[data.Weather == 'Fog']


# ## find all the instances when 'wheather' is clear or 'visiblity' is above 40? 

# In[13]:


data[(data.Weather =='Clear') | (data['Visibility_km'] > 40)]


# # Find alll the instances When :
# A) 'Weather is clear' and relative humidity is > 50
# or
# B) Visblity is above 40 

# In[5]:


data[(data.Weather=='Clear')&(data['Rel Hum_%'] >50) | (data['Visibility_km'] > 40) ]


# In[ ]:




