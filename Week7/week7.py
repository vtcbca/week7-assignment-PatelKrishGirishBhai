#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv


# In[ ]:


with open ('c:\sqlite3\csv\product_selling.csv','w') as wf:
    data=csv.writer(wf)
    header=["prod_no","prod_name","jan","feb","mar","apr","may","jun"]
    data.writerow(header)
    for i in range(12):
        prod_no=int(input("Enter product no:"))
        prod_name=input("Enter name:")
        jan=int(input("Enter product selling of jan:"))
        feb=int(input("Enter product selling of feb:"))
        mar=int(input("Enter product selling of mar:"))
        apr=int(input("Enter product selling of apr:"))
        may=int(input("Enter product selling of may:"))
        jun=int(input("Enter product selling of jun:"))
        record=[prod_no,prod_name,jan,feb,mar,apr,may,jun]
        data.writerow(record)


# In[ ]:


with open('c:\sqlite3\csv\product_selling.csv','r')as g1:
    content=csv.reader(g1)
    for i in content:
        print(i)


# In[ ]:


import pandas as pd
df=pd.read_csv('c:\sqlite3\csv\product_selling.csv')
print(df)


# In[ ]:


df.columns=["Product_no","Product_name","January","February","March","April","May","June"]
print(df)


# In[ ]:


df["Total sell"]=df["January"]+df["February"]+df["March"]+df["April"]+df["May"]+df["June"]
df
df["Average sell"]=df["Total sell"]/6
df


# In[ ]:


df.loc[12],df.loc[13]=[13,"laptop adptor",8000,10000,6000,7000,9000,12000,52000,8666.66],[14,"SSD",5000,6000,5000,4000,2000,8000,30000,5000]
df


# In[ ]:


df.loc[2.5]=[3,"charging",8000,6000,8000,5000,4000,6000,37000,6166.66]
df.loc[3.5]=[4,"SSD",8000,6000,9000,5000,8000,7000,43000,7166.666]
df


# In[ ]:


df.head(5)


# In[ ]:


df.tail(5)


# In[ ]:


df.iloc[5:9]


# In[ ]:


df["Product_name"]


# In[ ]:


df[["January","Product_no","Product_name"]]


# In[ ]:


df[(df.January>5000) & (df.February>8000)][["Product_no","Product_name"]]


# In[ ]:


df.sort_values(by=["Product_name"])


# In[ ]:


df.iloc[1::2]


# In[ ]:


df.iloc[::2]

