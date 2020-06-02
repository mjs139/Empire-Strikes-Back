#!/usr/bin/env python
# coding: utf-8

# # Reproducing Star Wars Analysis in Python
# 
# For this project, I will reproduce analysis done by [538](https://fivethirtyeight.com/features/americas-favorite-star-wars-movies-and-least-favorite-characters/) asking if American realizes that "The Empire Stikes Back" is the best of the Star Wars films. Their survey includes [835 responses] (https://github.com/fivethirtyeight/data/tree/master/star-wars-survey). 
# 
# For this project, I will be cleaning and exploring the data. 

# In[1]:


import pandas as pd
star_wars = pd.read_csv("star_wars.csv", encoding="ISO-8859-1")


# In[2]:


star_wars.head(10)


# In[4]:


star_wars.columns


# I will now remove any rows where the RespondentID is NaN. 

# In[6]:


star_wars = star_wars[pd.notnull(star_wars["RespondentID"])]
star_wars.head(10)


# I will now take a look at the following two columns:
# 
# -Have you seen any of the 6 films in the Star Wars franchise?
# - Do you consider yourself to be a fan of the Star Wars film franchise?
# 
# I will convert these columns in Boolean values. 

# In[7]:


yes_no = {
    "Yes": True,
    "No": False
}

first = "Have you seen any of the 6 films in the Star Wars franchise?"
second = "Do you consider yourself to be a fan of the Star Wars film franchise?"
star_wars[first] = star_wars[first].map(yes_no)
star_wars[second] = star_wars[second].map(yes_no)

star_wars.head()


# Now, for the 6 columns below, I will convert to a Boolean, and then rename the column to something more intuitive. 

# In[8]:


import numpy as np

movie_mapping = {
    "Star Wars: Episode I  The Phantom Menace": True,
    np.nan: False,
    "Star Wars: Episode II  Attack of the Clones": True,
    "Star Wars: Episode III  Revenge of the Sith": True,
    "Star Wars: Episode IV  A New Hope": True,
    "Star Wars: Episode V The Empire Strikes Back": True,
    "Star Wars: Episode VI Return of the Jedi": True
}

for col in star_wars.columns[3:9]:
    star_wars[col] = star_wars[col].map(movie_mapping)


# In[9]:


star_wars = star_wars.rename(columns={
        "Which of the following Star Wars films have you seen? Please select all that apply.": "seen_1",
        "Unnamed: 4": "seen_2",
        "Unnamed: 5": "seen_3",
        "Unnamed: 6": "seen_4",
        "Unnamed: 7": "seen_5",
        "Unnamed: 8": "seen_6"
        })

star_wars.head()


# Now, for the columns that ask respondents to rank the movies, I will convert each column to a numeric and then rename the columns

# In[10]:


star_wars = star_wars.rename(columns={
        "Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.": "ranking_1",
        "Unnamed: 10": "ranking_2",
        "Unnamed: 11": "ranking_3",
        "Unnamed: 12": "ranking_4",
        "Unnamed: 13": "ranking_5",
        "Unnamed: 14": "ranking_6"
        })

star_wars.head()


# In[11]:


star_wars[star_wars.columns[9:15]] = star_wars[star_wars.columns[9:15]].astype(float)


# I now want to find the highest ranked movie. First I will find the mean for each. 

# In[15]:


means = star_wars[star_wars.columns[9:15]].mean()
means


# In[17]:


get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt

plt.bar(range(6), means)


# Since the lower rankings here indicate the better film, it looks like the respondents felt that "Empire" was the best film. 

# I now want to see how many people have seen each film. 

# In[19]:


seens = star_wars[star_wars.columns[3:9]].sum()
plt.bar(range(6), seens)


# It looks like more people have seen the original trilogy than the prequels. The highest seen film is "Empire"

# I will now see how the following segments ranked the films: fans vs not fans

# In[21]:


fans = star_wars[star_wars["Do you consider yourself to be a fan of the Star Wars film franchise?"] == True]
not_fans = star_wars[star_wars["Do you consider yourself to be a fan of the Star Wars film franchise?"] == False]


# In[22]:


fan_means = fans[fans.columns[9:15]].mean()
fan_means


# In[23]:


not_fan_means = not_fans[fans.columns[9:15]].mean()
not_fan_means


# In[28]:


barWidth = 0.25

r1 = np.arange(len(fan_means))
r2 = [x + barWidth for x in r1]

plt.bar(r1, fan_means, color='#7f6d5f', width=barWidth, edgecolor='white', label='Fans')
plt.bar(r2, not_fan_means, color='#557f2d', width=barWidth, edgecolor='white', label='Not-Fans')

plt.legend()
plt.show()


# Why do non-fans like Episode 1? Why?
