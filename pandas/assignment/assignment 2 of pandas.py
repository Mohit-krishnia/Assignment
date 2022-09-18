
import pandas as pd
import numpy as np

# Assign it to a variable called users and use the 'user_id' as index
# here i save the raw data to my notpad and by upload in jupyter notebook i use it
user=pd.read_csv("data.txt",sep='|',index_col=0)

# printing first 10 and last 10 ro
pd.concat([user.iloc[:10],user.iloc[-10:]])

# What is the number of observations in the dataset
user.shape[0]

# What is the number of columns in the dataset
user.shape[1]

# Print the name of all the columns
user.columns

# How is the dataset indexed
user.index

# What is the data type of each column and DataFrame Info
user.info()

# Print only the occupation column
print(user['occupation'])

# How many different occupations are in this dataset
user['occupation'].value_counts().count()

# What is the most frequent occupation
user['occupation'].value_counts().idxmax()

# Describe all the columns
user.describe(include='all')

# Summarize only the occupation column
user['occupation'].value_counts()

# What is the mean age of users
user['age'].mean()

# What is the age with least occurrence
user['age'].value_counts().idxmin()

