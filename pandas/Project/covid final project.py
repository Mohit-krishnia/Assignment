import pandas as pd

df=pd.read_csv('covid.txt',sep=',')
df

# Find no. of rows & columns in the dataset
df.shape

# Data types of columns
df.dtypes

# Info & describe of data in dataframe
df.describe(include='all')

# Find count of unique values in location column
df['location'].unique()

# Find which continent has maximum frequency using values counts
df['continent'].value_counts()

# Find maximum & mean value in 'total_cases'
df['total_cases'].max()
df['total_cases'].mean()

# Find 25%,50% & 75% quartile value in 'total_deaths'
print("25% of total deaths is : ",df['total_cases'].quantile(.25))
print("50% of total deaths is : ",df['total_cases'].quantile(.50))
print("75% of total deaths is : ",df['total_cases'].quantile(.75))

#  Find which continent has maximum 'human_development_index'
idx = df.groupby(by=['continent','human_development_index'])['human_development_index'].max()
idx.sort_values(ascending=False)

# Find which continent has minimum 'gdp_per_capita'.
idx=df.groupby(by=['continent','gdp_per_capita'])['gdp_per_capita'].min()
idx.sort_values(ascending=True)

''# # Filter the dataframe with only this columns['continent','location','date','total_cases','total_deaths','gdp_per_capita','human_development_index']
# df_1=df.filter(['continent','location','date','total_cases','total_deaths','gdp_per_capita','human_development_index'])
# s=df.update(df_1)
# s
df1=df.groupby(by='continent')['continent','location','date','total_cases','total_deaths','gdp_per_capita','human_development_index']
df.update(df1)
df1.head()

#  Remove all duplicates observations
df.drop_duplicates()

# . Find missing values in all columns
df.isnull().sum()

#  Remove all observations where continent column value is missing
df.dropna(subset='continent')

# Fill all missing values with 0
df.fillna(0)

# Convert date column in datetime format using pandas.to_datetime
df['date']=pd.to_datetime(df['date']).dt.date
df

# Create new column month after extracting month data from date column
df['month']=pd.to_datetime(df['date']).dt.month
df

#. Find max value in all columns using groupby function on 'continent' column
df_1=df.groupby(by=['continent','location','date','total_cases','total_deaths','gdp_per_capita','human_development_index'])['continent'].size().sort_values(ascending=True).reset_index(name='find_max')
df_1

# . Store the result in a new dataframe named 'df_groupby'
df_groupby=df_1
df_groupby

#Create a new feature 'total_deaths_to_total_cases' by ratio of'total_deaths' column to 'total_cases'
df_groupby['total_deaths_to_total_cases']=df_groupby['total_deaths'].div(df_groupby['total_cases'])
df_groupby

# Perform Univariate analysis on 'gdp_per_capita' column by plotting
import seaborn as sns
sns.distplot(df_groupby['gdp_per_capita'],kde=True,color='red')

# Plot a scatter plot of 'total_cases' & 'gdp_per_capita
sns.scatterplot(df_groupby['gdp_per_capita'],df_groupby['total_cases'],color='red')

# Plot Pairplot on df_groupby dataset.
sns.pairplot(df_groupby)

# Plot a bar plot of 'continent' column with 'total_cases'
sns.catplot(data=df_groupby,x='continent',y='total_cases',kind='bar')

# .Save the df_groupby dataframe in your local drive using pandas.to_csv function
df_groupby.to_csv('Covid_Project.csv', index=False)

