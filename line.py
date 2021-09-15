import columns as columns
import inline as inline
import matplotlib as matplotlib
import numpy as np  # useful for many scientific computing in Python
import pandas as pd  # primary data structure library

df_can = pd.read_excel(
    'source/canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)

print('Data read into a pandas dataframe!')

# view the top 5 rows
df_can.head()

# view the bottom 5 rows
df_can.tail()

# When analyzing a dataset, it's always a good idea to start by getting basic information about your dataframe.
# We can do this by using the info() method.
# This method can be used to get a short summary of the dataframe.
df_can.info(verbose=False)

# To get the list of column headers we can call upon the data frame's columns instance variable, similarly, the index
df_can.columns
df_can.index

# To get the index and columns as lists
df_can.columns.tolist()
df_can.index.tolist()

# size of dataframe (rows, columns)
df_can.shape

# in pandas axis=0 represents rows (default) and axis=1 represents columns.
# remove some unnecessary data
df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
df_can.head(2)

# Let's rename the columns so that they make sense. We can use rename() method by passing in a dictionary of old and new names as follows
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
df_can.columns

# add a column, axis = 1 means columns, axis = 0 means rows
df_can['Total'] = df_can.sum(axis=1)

# quick summary of each column
df_can.describe()

# Select Column
# There are two ways to filter on a column name:
#
# Method 1: Quick and easy, but only works if the column name does NOT have spaces or special characters.
#
#     df.column_name               # returns series
# Method 2: More robust, and can filter on multiple columns.
#
#     df['column']                  # returns series
#     df[['column 1', 'column 2']]  # returns dataframe
df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]] # returns a dataframe
# notice that 'Country' is string, and the years are integers.

# There are main 2 ways to select rows:
#
#     df.loc[label]    # filters by the labels of the index/column
#     df.iloc[index]   # filters by the positions of the index/column

df_can.set_index('Country', inplace=True)
# tip: The opposite of set is reset. So to reset the index, we can use df_can.reset_index()

# find the full data of Japan, row 87
df_can.loc['Japan']
df_can.iloc[87]
df_can[df_can.index == 'Japan']

# find the data for Japan 2013 (index is 36)
df_can.loc['Japan', 2013]
df_can.iloc[87, 36]

# 3. for years 1980 to 1985
df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]]
df_can.iloc[87, [3, 4, 5, 6, 7, 8]]

# Column names that are integers (such as the years) might introduce some confusion. For example, when we are referencing the year 2013,
# one might confuse that when the 2013th positional index.
#
# To avoid this ambuigity, let's convert the column names into strings: '1980' to '2013'.
df_can.columns = list(map(str, df_can.columns))

# useful for plotting later on
years = list(map(str, range(1980, 2014)))

# filter data frame
# 1. create the condition boolean series
condition = df_can['Continent'] == 'Asia'

# 2. pass this condition into the dataFrame
df_can[condition]

# we can pass multiple criteria in the same line.
# let's filter for AreaNAme = Asia and RegName = Southern Asia
df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')]



# Matplotlib.Pyplot
import matplotlib as mpl
import matplotlib.pyplot as plt

# find the haiti data
haiti = df_can.loc['Haiti', years] # passing in years 1980 - 2013 to exclude the 'total' column
haiti.head()

# haiti.plot()
# plt.show()

haiti.index = haiti.index.map(int) # let's change the index values of Haiti to type integer for plotting
haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
# annotate the 2010 Earthquake.
# syntax: plt.text(x, y, label)
plt.text(2000, 6000, '2010 Earthquake') # see note below
#plt.show()

# find China data and display the dataframe
df_China = df_can.loc[['China'], years]
print(df_China)

# find China and india data and display the dataframe
df_CI = df_can.loc[['China', 'India'], years]
df_CI.plot(kind='line')
# plt.show()

# swap the row and columns
df_CI = df_CI.transpose()

df_CI.index = df_CI.index.map(int) # let's change the index values of df_CI to type integer for plotting
df_CI.plot(kind='line')

plt.title('Immigrants from China and India')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
# plt.show()

# find the top 5
inplace = True  # parameter saves the changes to the original df_can dataframe
# sort the dataframe
df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)

# get the top 5 entries
df_top5 = df_can.head(5)

# transpose the dataframe
df_top5 = df_top5[years].transpose()

# print(df_top5)

# Plot the dataframe. To make the plot more readable, we will change the size using the `figsize` parameter.
df_top5.index = df_top5.index.map(int)  # let's change the index values of df_top5 to type integer for plotting
df_top5.plot(kind='line', figsize=(14, 8))  # pass a tuple (x, y) size

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()

# area plot
# let's change the index values of df_top5 to type integer for plotting
# df_top5.index = df_top5.index.map(int)
# df_top5.plot(kind='area',
#              alpha=0.25,  # 0 - 1, default value alpha = 0.5
#              stacked=False,
#              figsize=(20, 10))  # pass a tuple (x, y) size
#
# plt.title('Immigration Trend of Top 5 Countries')
# plt.ylabel('Number of Immigrants')
# plt.xlabel('Years')
#
# plt.show()

# hist for histogram
# np.histogram returns 2 values
# count, bin_edges = np.histogram(df_can['2013'])

# print(count) # frequency count
# print(bin_edges) # bin ranges, default = 10 bins
# df_can['2013'].plot(kind='hist', figsize=(8, 5), xticks=bin_edges)
#
# # add a title to the histogram
# plt.title('Histogram of Immigration from 195 Countries in 2013')
# # add y-label
# plt.ylabel('Number of Countries')
# # add x-label
# plt.xlabel('Number of Immigrants')
#
# plt.show()
# anothter way generate histogram
# df_can.loc[['Denmark', 'Norway', 'Sweden'], years].plot.hist()

# # let's get the x-tick values
# count, bin_edges = np.histogram(df_t, 15)
#
# # un-stacked histogram
# df_t.plot(kind ='hist',
#           figsize=(10, 6),
#           bins=15,
#           alpha=0.6,
#           xticks=bin_edges,
#           color=['coral', 'darkslateblue', 'mediumseagreen']
#          )
#
# plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
# plt.ylabel('Number of Years')
# plt.xlabel('Number of Immigrants')
#
# plt.show()

# pie chart
# # group countries by continents and apply sum() function
# df_continents = df_can.groupby('Continent', axis=0).sum()
#
# # note: the output of the groupby method is a `groupby' object.
# # we can not use it further until we apply a function (eg .sum())
# print(type(df_can.groupby('Continent', axis=0)))

# colors_list = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink']
# explode_list = [0.1, 0, 0, 0, 0.1, 0.1] # ratio for each continent with which to offset each wedge.
#
# df_continents['Total'].plot(kind='pie',
#                             figsize=(15, 6),
#                             autopct='%1.1f%%',
#                             startangle=90,
#                             shadow=True,
#                             labels=None,         # turn off labels on pie chart
#                             pctdistance=1.12,    # the ratio between the center of each pie slice and the start of the text generated by autopct
#                             colors=colors_list,  # add custom colors
#                             explode=explode_list # 'explode' lowest 3 continents
#                             )
#
# # scale the title up by 12% to match pctdistance
# plt.title('Immigration to Canada by Continent [1980 - 2013]', y=1.12)
#
# plt.axis('equal')
#
# # add legend
# plt.legend(labels=df_continents.index, loc='upper left')
#
# plt.show()

# scatter plot and prediction by using polyfit
# # we can use the sum() method to get the total population per year
# df_tot = pd.DataFrame(df_can[years].sum(axis=0))
#
# # change the years to type int (useful for regression later on)
# df_tot.index = map(int, df_tot.index)
#
# # reset the index to put in back in as a column in the df_tot dataframe
# df_tot.reset_index(inplace = True)
#
# # rename columns
# df_tot.columns = ['year', 'total']
#
# # view the final dataframe
# df_tot.head()
#
# x = df_tot['year']      # year on x-axis
# y = df_tot['total']     # total on y-axis
# fit = np.polyfit(x, y, deg=1) # deg: Degree of fitting polynomial. 1 = linear, 2 = quadratic, and so on
#
# fit
#
# df_tot.plot(kind='scatter', x='year', y='total', figsize=(10, 6), color='darkblue')
#
# plt.title('Total Immigration to Canada from 1980 - 2013')
# plt.xlabel('Year')
# plt.ylabel('Number of Immigrants')
#
# # plot line of best fit
# plt.plot(x, fit[0] * x + fit[1], color='red') # recall that x is the Years
# plt.annotate('y={0:.0f} x + {1:.0f}'.format(fit[0], fit[1]), xy=(2000, 150000))
#
# plt.show()
#
# # print out the line of best fit
# 'No. Immigrants = {0:.0f} * Year + {1:.0f}'.format(fit[0], fit[1])




# other plots
# bar for vertical bar plots
# barh for horizontal bar plots
# hist for histogram
# box for boxplot
# kde or density for density plots
# area for area plots
# pie for pie plots
# scatter for scatter plots
# hexbin for hexbin plot



