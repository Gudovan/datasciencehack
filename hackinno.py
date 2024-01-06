#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
rfile = pd.read_csv('movies.csv')
rfile.head()


# In[5]:


print(rfile.shape)


# In[6]:


rating = pd.read_csv('ratings.csv')
rating.head()


# In[7]:


print(rating.shape)


# In[10]:


unique_users = rating.userId.unique()


# In[11]:


print(len(unique_users))


# In[12]:


rating.movieId.value_counts()


# In[18]:


print(rfile[rfile['movieId'] == 356])


# In[20]:


tags = pd.read_csv('tags.csv')
tags.head()


# In[21]:


# movie id of Matrix, The (1999)
print(rfile[rfile['title'] == 'Matrix, The (1999)'])


# In[22]:


# movieId of Matrix, The (1999) = 2571
frame = pd.DataFrame(tags[tags['movieId']==2571])


# In[23]:


# tags for Matrix 
frame


# In[24]:


# movieId for Terminator 2: Judgment Day (1991)
print(rfile[rfile['title']=='Terminator 2: Judgment Day (1991)'])


# In[25]:


# movieId for Terminator 2 is 589
# rating table with movieId = 589
# What is the average user rating for movie named "Terminator 2: Judgment Day (1991)"?
ar = pd.DataFrame(rating[rating['movieId']==589])
print(ar)


# In[34]:


import statistics
x = sum(ar['rating'])
print(x)
# rows = 224
avg = x/224
print(avg)
print(statistics.mean(ar['rating']))


# In[35]:


#How does the data distribution of user ratings for "Fight Club (1999)" movie looks like?
# 1. movieId of Fight Club

print(rfile[rfile['title']=='Fight Club (1999)'])


# In[36]:


#movieId = 2959

fcdf = pd.DataFrame(rating[rating['movieId']==2959])
print(fcdf)


# In[37]:


import matplotlib.pyplot as plt
fcdf['rating'].hist()
plt.show()
#left skewed histogram


# In[38]:


# Which movie is the most popular based on  average user ratings? *
#Godfather, The (1972)
#Shawshank Redemption, The (1994)
#Jumanji (1995)
#Wolf of Wall Street, The (2013)


# In[ ]:


1. Group the user ratings based on movieId and apply aggregation operations like count and mean on ratings. 
2. Apply inner join on dataframe created from movies.csv and the grouped df from step 1.
3. Filter only those movies which have more than 50 user ratings (i.e. > 50).


# In[99]:


# 1
modified_ratings = pd.DataFrame()
modified_ratings['movieId'] = rating.movieId.unique()
modified_ratings


# In[88]:


lst = rating[rating['movieId']==1]


# In[103]:


rating_list = list(lst['rating'])
print(len(rating_list))
print(statistics.mean(rating_list))


# In[100]:


count = 0
for i in modified_ratings['movieId']:
    r = rating[rating['movieId']==i]
    r_l = list(r['rating'])
    modified_ratings.at[count,'ratings_count']=len(r_l) 
    modified_ratings.at[count,'ratings_mean']=statistics.mean(r_l)
    count+=1
    


# In[101]:


modified_ratings.head()


# In[104]:


new_rfile = rfile.copy()


# In[108]:


new_rfile=new_rfile.merge(modified_ratings, on='movieId')


# In[109]:


new_rfile


# In[110]:


count_fifty = pd.DataFrame(new_rfile[new_rfile['ratings_count']>50])


# In[111]:


count_fifty


# In[113]:


sorted_cf=count_fifty.sort_values(by='ratings_mean', ascending=False)


# In[118]:


sorted_cf.head(10)


# In[115]:


no_sort = count_fifty.sort_values(by='ratings_count', ascending=False)


# In[117]:


no_sort.head(20)


# In[120]:


pip install BeautifulSoup4


# In[ ]:




