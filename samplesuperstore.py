#!/usr/bin/env python
# coding: utf-8

# ### Author - T Ompriya Subudhi

# ### The Sparks Foundation - GRIPMARCH23 

# ### Data Science and Business Analytics Intern 

# ### Task - 3  Exploratory Data Analysis - Retail

# ### Problem Statement - To find out the weak areas where profit can be increased
# 

# In[1]:


# importing libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings(action = 'ignore')


# #### Loading  the SampleSuperstore Data Set 

# In[2]:


df = pd.read_csv(r'C:\Users\acer\Desktop\tsf\SampleSuperstore.csv')


# In[3]:


df


# In[4]:


df.shape


# #### There are 9994 rows and 13 columns are present  in the given dataset 

# In[5]:


df.head()


# In[6]:


df.tail()


# In[7]:


df.columns


# In[8]:


df.info()


# In[9]:


df.isnull().sum()


# #### The dataset contains zero null values

# In[10]:


df.duplicated().sum()


# #### 17 duplicate values are present. 

# In[11]:


# dropping the duplicated values
df = df.drop_duplicates().reset_index().drop(['index'],axis = 'columns')


# In[12]:


# rechecking duplicated rows
df.duplicated().sum()   


# In[13]:


df.shape


# #### After dropping duplicated rows the new shape is 9977 rows and 13 columns

# In[14]:


# dropping Postal Code column as it has no use
df.drop(['Postal Code'],axis = 1,inplace = True)


# In[15]:


df.shape


# #### Postal Code column has been removed 

# In[16]:


df.describe()


# In[17]:


# boxplot to detect outliers
plt.figure(figsize = (12,7))
plt.title('Box Plot to detect outliers',fontsize = 16)
df.boxplot(patch_artist = True,color = 'orange')
plt.show()


# #### 1. Quantity  and Discount have no outliers whereas Sales and Profit have outliers                                               
# #### 2. But we can't remove these outliers beacuse it will affect our result

# ### Analyzing other variables 

# In[18]:


# analysis of shipment variable
plt.figure(figsize = (10,6))
ship_mode = df['Ship Mode'].value_counts()
ship_mode.plot(kind = 'bar',color = '#7eb54e')
plt.title('Performances of Ship Mode',fontsize = 14)
plt.show()


# #### Standard class ship mode prefered by most of the customers

# In[19]:


# analysis of segment variable
segment = df['Segment'].value_counts()
plt.plot(segment,color = 'r',linewidth = '12')
plt.ylabel('Value Counts',color = 'r',fontsize = 14)
plt.xlabel('Types of Segment',color = 'r',fontsize = 14)
plt.title('Distribution of Segment',fontsize = 16,color = 'r')
plt.show()


# #### We can see consumer segment widely  prefered by customers

# In[20]:


# analyzing country variable
plt.figure(figsize = (6,4))
sns.histplot(df['Country'],color = 'purple')
plt.show()


# #### Data set has only one country i.e, United State so we can drop this column

# In[21]:


df.drop(['Country'],axis = 1,inplace = True)
df.shape


# #### Country column has been removed 

# In[22]:


# analyzing city variable
plt.figure(figsize = (16,10))
sns.countplot(data = df,y= 'City',order = df.City.value_counts().iloc[:50].index)
plt.title('Top 50 cities',fontsize = 18)
plt.show()


# #### New York city has more value counts followed by Los Angeles ,Philadelphia 

# In[23]:


# bottom cities
plt.figure(figsize = (16,10))
df.City.value_counts().nsmallest(30).plot(kind = 'bar',color = 'pink',width = 0.4)
plt.title('Bottom 30 cities',fontsize = 16)
plt.show()


# #### We must focus on these cities to make more profit 

# In[24]:


# analyzing state variable
plt.figure(figsize = (18,10))
sns.histplot(data = df,x = 'State')
plt.xticks(rotation = 90)
plt.show()


# #### We have to focus on Wyoming,West Virgina,Maine states 
# #### California have highest counts followed by New York

# In[25]:


# analyzing region variable
plt.figure(figsize=(10,7))
values = df['Region'].value_counts()
labels = df['Region'].unique().tolist()
explode = (0.2,0,0,0)
plt.pie(values,labels=labels,explode = explode,autopct = '%1.2f%%')
plt.show()


# #### We most focus on East and Central region where profit can be increased 

# In[26]:


# analyzing category variable
plt.figure(figsize = (8,6))
sns.histplot(data = df,x = 'Category',edgecolor = 'g',color = 'pink')
plt.title('Disribution of Category',fontsize = 16)
plt.xlabel('Types of Category',fontsize = 12)
plt.ylabel('Count',fontsize = 12)
plt.show()


# #### Most of the customers prefers Office Supplies whereas Furniture and Technology category have almost equal value counts

# In[27]:


# analyzing subcategory variable
plt.figure(figsize = (12,8))
sns.histplot(data =df,x='Sub-Category',color = 'r',edgecolor = 'k')
plt.title('Disribution of Sub-Category',fontsize = 16)
plt.xlabel('Types of Sub-Category',fontsize = 12)
plt.ylabel('Count',fontsize = 12)
plt.xticks(rotation = '90')
plt.show()


# #### Brinders and Paper have highest count 
# #### We most focus on other sub category such as Copiers,machines etc. to increase their sales

# In[28]:


# analyzing sales variable
plt.figure(figsize = (12,6))
sns.histplot(df.Sales,kde = True)
plt.title("Histogram of sales",fontsize = 18)
plt.xlabel("Sales",fontsize = 14)
plt.ylabel("Count",fontsize = 14)
plt.show()


# #### Maximum sales count lies between 0 to 170 and some of them are beyond 4000

# In[29]:


# analyzing quantity
plt.figure(figsize = (12,6))
sns.histplot(df.Quantity,kde = True,color = 'Orange')
plt.title("Histogram of Quantity",fontsize = 18)
plt.xlabel("Quantity",fontsize = 14)
plt.ylabel("Count",fontsize = 14)
plt.show()


# #### Generally amount of quantity lies between 1 to 9 and it is rare when customers order quantity more than 10

# In[30]:


#analyzing discount variable
plt.figure(figsize = (14,7))
sns.histplot(df.Discount,kde = True,color = 'g')
plt.title("Histogram of Discount",fontsize = 18)
plt.xlabel("Discount",fontsize = 14)
plt.ylabel("Count",fontsize = 14)
plt.show()


# #### Usual discount is 20% 

# In[31]:


# boxplot for profit 
plt.figure(figsize=(16,9))
sns.boxplot(df['Profit'])
plt.show()


# #### Profit column has very few outliers and we can't remove these outliers as it will affect our original result 

# In[32]:


# analysing Profit varialbe
plt.figure(figsize = (14,9))
sns.histplot(df.Profit,kde = True,color = 'brown')
plt.title("Histogram of Profit",fontsize = 18)
plt.xlabel("Profit",fontsize = 14)
plt.show()


# #### Most of the profit lies between 0 to 600  

# ## Analyzing numeric variables together 

# In[33]:


# analyzing Sales,Quantity,Discount,Profit
sns.pairplot(data = df,palette = 'bright',diag_kind = 'kde')
plt.show()


# In[34]:


# analyzing correlation 
plt.figure(figsize = (9,7))
sns.heatmap(df.corr(),annot = True,linewidth = 1,linecolor = 'k',cmap = 'tab20')
plt.show()


# ####  Sales and Quantity have positive relation with Profit whereas Discount has negative relation with Profit

# #### Sales and Profit are highly correlated 

# In[35]:


# sales vs profit
plt.figure(figsize=(14,8))
plt.scatter(x = df['Sales'],y = df['Profit'],color = 'red')
plt.title("sales vs Profit",fontsize = 18)
plt.show()


# In[36]:


# profit vs discount
plt.figure(figsize=(14,8))
plt.scatter(x = df['Sales'],y = df['Discount'],color = 'g')
plt.title("sales vs Discount",fontsize = 18)
plt.show()


# In[37]:


# analyzing shipmode by sales and profit
df_ship = df.groupby('Ship Mode')['Sales','Profit'].agg(sum)
df_ship.plot(kind = 'bar',color = ['pink','g'])
plt.title('Sales and Profit by different Shipmode',fontsize = 15)
plt.ylabel('Total Sales and Profit')
plt.show()


# #### Standard Class makes more sales and more profit and we have to focus on same day in order to increase profit 

# In[38]:


# analyzing segment by sales and profit
df_segment = df.groupby('Segment')['Sales','Profit'].agg(sum)
df_segment.plot(kind = 'bar',color = ['red','blue'])
plt.title('Sales and Profit by different Segment',fontsize = 15)
plt.ylabel('Total Sales and Profit')
plt.show()


# #### Consumer segment has highest sale and profit 

# In[39]:


# analyzing region by sales and profit
df_region = df.groupby('Region')['Sales','Profit'].agg(sum)
df_region.plot(kind = 'bar',color = ['brown','yellow'])
plt.title('Sales and Profit by different Region',fontsize = 15)
plt.ylabel('Total Sales and Profit')
plt.show()


# #### West and East region gives more sales and profit on the contrary south region has highest value counts
# #### So we should focus on Central and South region

# In[40]:


# analyzing category by sales and profit
df_category = df.groupby('Category')['Sales','Profit'].agg(sum)
df_category.plot(kind = 'bar',color = ['orange','k'])
plt.title('Sales and Profit by different Category',fontsize = 15)
plt.ylabel('Total Sales and Profit')
plt.show()


# #### Technology has more profit and sales. Office supplies has highest value counts but less sale and profit 

# In[41]:


# analyzing sub category
df_sub = df.groupby('Sub-Category')['Profit','Sales'].agg(sum)
df_sub.plot(kind = 'bar',color = ['blue','green'])
plt.title('Sales and Profit by different Sub Category',fontsize = 15)
plt.ylabel('Total Sales and Profit')
plt.show()


# #### Chairs and Phones have highest sale but makes less profit ,copiers and paper makes more profit with tables gives us lowest profit

# ## Conclusion: 
1.Standard Class shipmode is preferred by most of the customers also it makes more sales and profit.
2.We should focus on same day Delivary.
3.Consumer segment has highest value counts as well as gives more profit,need to focus on Home office segment.
4.Dataset has only one country i.e,United States,so we drop this column.
5.New York city has maximum value counts followed by Los Angeles ,Philadelphia.
6.We must focus on bottom 30 cities in order to increase profit.
7.California state mostly preferred followed by New York,have to focus on Wyoming,West Virgina,Maine states.
8.West and East region gives more sales and profit on the contrary south region has highest value counts
  So we should focus on Central and South region.
9.Technology category has more profit and sales. Office supplies has highest value counts but less sale and profit.
10.Chairs and Phones have highest sale but makes less profit,Brinders and Paper have highest demand.
11.We most focus on other sub category such as Copiers,machines etc. to increase their sales by giving discount.
12.Art Sub-Category have the heighest profit with least discount, so we must promote more Art category product
13.Sales and Quantity have positive relation with Profit whereas Discount has negative relation with Profit
  Sales and Profit are highly correlated.
14.Maximum sales count lies between 0 to 170 and some of them are beyond 4000
15.Generally amount of quantity lies between 1 to 9 and it is rare when customers order quantity more than 10
16.Usual discount is 20%,we should minimize discount to make more profit. 
17.Overally,we should focus on weak regions,cities,states to increase profit.