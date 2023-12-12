# -*- coding: utf-8 -*-
"""Amazon Sale analysis .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kbjE8RrjMrxt9k9RyRNueiR9PVuOeX_S
"""

# Commented out IPython magic to ensure Python compatibility.
#libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

#read csv file by using pandas
aw = pd.read_csv("/content/amazon.csv")
aw.shape

#show first 10 rows
aw.head(10)

#information about columns
aw.info()

#list of columns
aw.columns

#data type of column
aw.dtypes

#cleaning the data and convert the data type
aw['discounted_price'] = aw['discounted_price'].str.replace('₹','')
aw['discounted_price'] = aw['discounted_price'].str.replace(",",'')
aw['discounted_price'] = aw['discounted_price'].astype('float64')

aw['actual_price'] = aw['actual_price'].str.replace('₹','')
aw['actual_price'] = aw['actual_price'].str.replace(",",'')
aw['actual_price'] = aw['actual_price'].astype('float64')

#cleaning the data and convert the data type
aw['discount_percentage'] = aw['discount_percentage'].str.replace('%','').astype('float64')
aw['discount_percentage'] = aw['discount_percentage']/100
aw['discount_percentage']

aw['rating'].value_counts()

#cleaning the data and convert the data type
aw['rating'] = aw['rating'].str.replace('|','4.0').astype('float64')

aw['rating'].value_counts()

#cleaning the data and convert the data type
aw['rating_count'] = aw['rating_count'].replace(',', '', regex=True)  # Remove commas

# Check if the column is of numeric type before converting
aw['rating_count'] = aw['rating_count'].astype('float64')

aw.info()

#remove duplicate values
duplicates = aw.duplicated()
aw[duplicates]

aw.isna().sum()

#copying data to another dataframe
aw1= aw[['product_id','product_name','category','discounted_price','actual_price','discount_percentage','rating','rating_count']].copy()

aw1.info()

#split the category feature
catsplit = aw['category'].str.split('|',expand = True)
catsplit

#naming the columns
catsplit = catsplit.rename(columns={0:'category_1', 1:'category_2', 2:'category_3'})

catsplit

#add those columns into previous dataframe
aw1['category_1'] = catsplit['category_1']
aw1['category_2'] = catsplit['category_2']
aw1

aw1.info()

#removing category column
aw1.drop(columns = 'category',inplace = True)

aw1.info()

aw1['category_1'].value_counts()

#convert column name into proper way
aw1['category_1'] = aw1['category_1'].str.replace('&', ' & ')
aw1['category_1'] = aw1['category_1'].str.replace('OfficeProducts', 'Office Products')
aw1['category_1'] = aw1['category_1'].str.replace('MusicalInstruments', 'Musical Instruments')
aw1['category_1'] = aw1['category_1'].str.replace('HomeImprovement', 'Home Improvement')

aw1['category_1'].value_counts()

aw1['category_2'].value_counts()

#convert column name into proper way
aw1['category_2'] = aw1['category_2'].str.replace('&', ' & ')
aw1['category_2'] = aw1['category_2'].str.replace(',', ', ')
aw1['category_2'] = aw1['category_2'].str.replace('HomeAppliances', 'Home Appliances')
aw1['category_2'] = aw1['category_2'].str.replace('AirQuality', 'Air Quality')
aw1['category_2'] = aw1['category_2'].str.replace('WearableTechnology', 'Wearable Technology')
aw1['category_2'] = aw1['category_2'].str.replace('NetworkingDevices', 'Networking Devices')
aw1['category_2'] = aw1['category_2'].str.replace('OfficePaperProducts', 'Office Paper Products')
aw1['category_2'] = aw1['category_2'].str.replace('ExternalDevices', 'External Devices')
aw1['category_2'] = aw1['category_2'].str.replace('DataStorage', 'Data Storage')
aw1['category_2'] = aw1['category_2'].str.replace('HomeStorage', 'Home Storage')
aw1['category_2'] = aw1['category_2'].str.replace('HomeAudio', 'Home Audio')
aw1['category_2'] = aw1['category_2'].str.replace('GeneralPurposeBatteries', 'General Purpose Batteries')
aw1['category_2'] = aw1['category_2'].str.replace('BatteryChargers', 'Battery Chargers')
aw1['category_2'] = aw1['category_2'].str.replace('CraftMaterials', 'Craft Materials')
aw1['category_2'] = aw1['category_2'].str.replace('OfficeElectronics', 'Office Electronics')
aw1['category_2'] = aw1['category_2'].str.replace('PowerAccessories', 'Power Accessories')
aw1['category_2'] = aw1['category_2'].str.replace('CarAccessories', 'Car Accessories')
aw1['category_2'] = aw1['category_2'].str.replace('HomeMedicalSupplies', 'Home Medical Supplies')
aw1['category_2'] = aw1['category_2'].str.replace('HomeTheater', 'Home Theater')

aw1['category_2'].value_counts()

aw1['product_id'].str.strip()

aw1['rating'].value_counts()

rating_score =[]
for score in aw1['rating']:
  if score < 2.0:rating_score.append('poor')
  elif score < 3.0:rating_score.append('below average')
  elif score <4.0:rating_score.append('average')
  elif score <5.0:rating_score.append('above average')
  elif score == 5.0:rating_score.append('excellent')

rating_score

aw1['rating_score'] = rating_score
aw1['rating_score'] = aw1['rating_score'].astype('category')

aw1['rating_score_ordered'] = pd.Categorical(aw1['rating_score'], categories=['Below Average', 'Average', 'Above Average', 'Excellent'], ordered=True)

aw1['difference_price'] = aw1['actual_price'] - aw1['discounted_price']

aw1.columns

aw1.head()

reviewers = aw[['user_id','user_name']]
reviewers

reviewer_id_split = reviewers['user_id'].str.split(',',expand = False)
reviewer_id_split

reviewer_id_exp = reviewer_id_split.explode()
reviewer_id_exp

reviewer_id_clean = reviewer_id_exp.reset_index(drop = True)
reviewer_id_clean

reviewer_name_split = reviewers['user_name'].str.split(',',expand = False)
reviewer_name_split

reviewer_name_exp = reviewer_name_split.explode()
reviewer_name_clean = reviewer_name_exp.reset_index(drop = True)
reviewer_name_clean

aw21 = pd.DataFrame(data = reviewer_id_clean)
aw22 = pd.DataFrame(data = reviewer_name_clean)

aw2 = pd.merge(aw21,aw22,left_index = True,right_index=True)
aw2.head()

"""DATA EXPLORATION

"""

sns.set_style(style = 'darkgrid')
sns.set_palette(palette = 'icefire')

"""Observation - 1 : Product Category"""

#pivot table
main_sub =  aw1[['category_1','category_2','product_id']]
main_sub = main_sub.rename(columns = {'category_1' :'Main Category', 'category_2' : 'Sub-Category', 'product_id':'Product ID'})
main_sub_piv = pd.pivot_table(main_sub,index = ['Main Category', 'Sub-Category'],aggfunc = 'count')
main_sub_piv

#bar graph
most_main_item = aw1['category_1'].value_counts().head(5).rename_axis('category_1').reset_index(name = 'counts')

most_sub_items = aw1['category_2'].value_counts().head(10).rename_axis('category_2').reset_index(name = 'counts')

fig,ax = plt.subplots( 2, 1,figsize = (8,10))
fig.suptitle('Most Amount of Products by Category',fontweight = 'heavy',size = 'x-large')

sns.barplot(ax = ax[0],data =most_main_item,x = 'counts',y = 'category_1' )
sns.barplot(ax = ax[1],data =most_sub_items,x = 'counts',y = 'category_2' )

plt.subplots_adjust(hspace = 0.3)

ax[0].set_xlabel('count',fontweight = 'bold')
ax[0].set_ylabel('Product Main Category',fontweight = 'bold')

ax[1].set_xlabel('count',fontweight = 'bold')
ax[1].set_ylabel('Most Products by Sub-Category',fontweight = 'bold')

ax[0].bar_label(ax[0].containers[0])
ax[1].bar_label(ax[1].containers[0])

plt.show()

#bar graph
disc_exp = sns.barplot(data = aw1.sort_values('discounted_price', ascending=False).head(5),x = 'discounted_price', y = 'product_name')
disc_exp.set_title('Top 5 Most Expensive Products After Discount',fontweight = 'bold')
disc_exp.set_xlabel('Discounted Price (Rupee India)', fontweight='bold')
disc_exp.set_ylabel('Product Name', fontweight='bold')
for bars in disc_exp.containers:
  disc_exp.bar_label(bars)
plt.show()

#bar graph
disc_chep = sns.barplot(data = aw1.sort_values('discounted_price').head(5),x= 'discounted_price',y = 'product_name')

disc_chep.set_title('Top 5 Cheapest Products After Discount', fontweight='bold')
disc_chep.set_xlabel('Discounted Price (Rupee India)', fontweight='bold')
disc_chep.set_ylabel('Product Name', fontweight='bold')
for bars in disc_chep.containers:
  disc_chep.bar_label(bars)
plt.show()

#bar graph
dif_price_large = sns.barplot(data = aw1.sort_values('difference_price', ascending=False).head(5),x = 'difference_price',y ='product_name' )
dif_price_large.set_title('Top 5 Products with the Largest Price Difference', fontweight='bold')
dif_price_large.set_xlabel('Price Difference (Rupee India)', fontweight='bold')
dif_price_large.set_ylabel('Product Name', fontweight='bold')
for bars in dif_price_large.containers:
  dif_price_large.bar_label(bars)
plt.show()

"""Observation 2: Correlation between Features

"""

fig, ax = plt.subplots(2,1,figsize=(8,10))
fig.suptitle('Correlation Between Features',fontweight = 'heavy',size = 'xx-large')

sns.heatmap(ax = ax[0],data = aw1.corr())
sns.scatterplot(ax = ax[1], data = aw1,x='discounted_price',y = 'actual_price',color = 'brown')
plt.subplots_adjust(hspace=0.8)
ax[1].set_xlabel('Actual Price (Rupee India)', fontweight='bold')
ax[1].set_ylabel('Discounted Price (Rupee India)', fontweight='bold')

ax[0].set_title('Heatmap', fontweight='bold')
ax[1].set_title('Correlation between Actual Price & Discounted Price', fontweight='bold')
plt.show()

"""Observation 3: Product Ratings"""

fig, ax = plt.subplots(1,2,figsize = (15,5))
fig.suptitle('Rating & Amount of Ratings Distribution', fontweight='heavy', size='xx-large')
fig.tight_layout(pad = 3.0)
sns.histplot(ax=ax[0],data = aw1,x = 'rating',bins = 15,kde = True,color = 'blue' )
sns.histplot(ax = ax[1],data = aw1,x='rating_count',bins = 10,kde = True,color ='purple')
ax[0].set_xlabel('Rating', fontweight='bold')
ax[1].set_xlabel('Amount of Ratings', fontweight='bold')

ax[0].set_ylabel('Count', fontweight='bold')
ax[1].set_ylabel('Count', fontweight='bold')

ax[0].set_title('Rating Distribution', fontweight='bold')
ax[1].set_title('Amount of Ratings Distribution', fontweight='bold')

plt.show()

fig, ax = plt.subplots(figsize = (10,6))
sns.boxplot(ax=ax,data = aw1,x='rating',y = 'category_1')
ax.set_xlabel('Rating',fontweight = 'bold')
ax.set_ylabel('Product Main Category', fontweight='bold')
ax.set_title('Rating Distribution by Product Main Category', fontweight='heavy', size='x-large', y=1.03)
plt.show()

rate_main_cat = aw1.groupby(['category_1','rating_score']).agg('count').iloc[:,1].rename_axis().reset_index(name = 'Amount')
rate_main_cat = rate_main_cat.rename(columns={'category_1' : 'Main Category', 'rating_score' : 'Rating Category'})
rate_main_cat

fig, ax =plt.subplots(figsize = (12,7))
sns.boxplot(ax=ax,data = aw1,x='rating',y = 'category_2')
ax.set_xlabel('Rating', fontweight='bold')
ax.set_ylabel('Product Main Category', fontweight='bold')
ax.set_title('Rating Distribution by Product Sub-Category', fontweight='heavy', size='x-large', y=1.03)
plt.show()

def p25(g):
    return np.percentile(g,25)
def p75(g):
    return np.percentile(g,75)

rating_pivot = aw1.pivot_table(values=['rating','rating_count'],index =['category_1','category_2'], aggfunc=([p25,np.median,np.mean,p75]))

rating_pivot = rating_pivot.rename(columns ={'rating':'Rating', 'rating_count': 'Rating Count', 'median':'Median', 'mean':'Mean'},index ={'category_1': 'Main Category', 'category_2': 'Sub Category'})

rating_pivot



"""Observation 3: Reviewers"""

top_reviewer = data = aw2['user_name'].value_counts().head(10).rename_axis('username').reset_index(name = 'counts')
top_review_plot = sns.barplot(data = top_reviewer,x='counts',y='username')
top_review_plot.bar_label(top_review_plot.containers[0])
top_review_plot.set_xlabel('Amount of Rating Reviews Given', fontweight='bold')
top_review_plot.set_ylabel("Reviewer's Name", fontweight='bold')
top_review_plot.set_title('Top 10 Active Reviewers', fontweight='heavy', size='x-large', y=1.03)
plt.show()

"""Observation 4: Product Pricing"""

fig, ax = plt.subplots(1,2,figsize=(15,5))
fig.suptitle('Actual Price & Discounted Price Distribution', fontweight='heavy', size='xx-large')

fig.tight_layout(pad = 3.0)

sns.histplot(ax=ax[0],data=aw1,x='actual_price',bins = 8,kde = True,color = 'red')
sns.histplot(ax=ax[1],data=aw1,x='discounted_price',bins=8,kde = True,color='orange')

ax[0].set_xlabel('Actual Price (Rupee India)', fontweight='bold')
ax[1].set_xlabel('Discounted Price (Rupee India)', fontweight='bold')

ax[0].set_ylabel('Count', fontweight='bold')
ax[1].set_ylabel('Count', fontweight='bold')

ax[0].set_title('Count', fontweight='bold')
ax[1].set_title('Discounted Price Distribution', fontweight='bold')
plt.show()

disc_hist = sns.histplot(data = aw1,x = 'discount_percentage',bins=8,kde =  True,color = 'green')
disc_hist.set_xlabel('Discount Percentage', fontweight='bold')
disc_hist.set_ylabel('Count', fontweight='bold')
disc_hist.set_title('Discount Percentage Distribution', fontweight='heavy', size='x-large')
plt.show()

aw1['discount_percentage'].describe()

fig, ax = plt.subplots(figsize = (10,6))
sns.boxplot(data = aw1,x='discount_percentage',y = 'category_1')
ax.set_xlabel('Discount Percentage', fontweight='bold')
ax.set_ylabel('Product Main Category', fontweight='bold')
ax.set_title('Discount Percentage Range by Product Main Category', fontweight='heavy', size='x-large', y=1.03)
plt.show()

fig, ax =plt.subplots(figsize=(12,7))
sns.boxplot(data = aw1,x ='discount_percentage',y='category_2')
ax.set_xlabel('Discount Percentage', fontweight='bold')
ax.set_ylabel('Product Sub-Category', fontweight='bold')
ax.set_title('Discount Range by Product Sub-Category', fontweight='heavy', size='x-large', y=1.03)
plt.show()

fig, ax = plt.subplots(2,1,figsize=(13,15))
fig.suptitle('Price Range by Product Main Category', fontweight='heavy', size='x-large')

sns.scatterplot(ax=ax[0],data = aw1,x = 'actual_price',y='category_1',alpha = 0.3,color = 'red')
sns.scatterplot(ax=ax[1],data = aw1,x='discounted_price',y='category_1',alpha = 0.3,color ='orange')

ax[0].set_xlabel('Actual Price (Rupee India)', fontweight='bold')
ax[0].set_ylabel('Product Main Category', fontweight='bold')
ax[0].set_title('Actual Price Range by Product Main Category', fontweight='bold')

ax[1].set_xlabel('Discounted Price (Rupee India)', fontweight='bold')
ax[1].set_ylabel('Product Main Category', fontweight='bold')
ax[1].set_title('Product Main Category', fontweight='bold')
plt.subplots_adjust(hspace = 0.3)
plt.show()

fig, ax = plt.subplots(2,1,figsize=(13,15))
fig.suptitle('Price Range by Product Main Category', fontweight='heavy', size='x-large')
sns.scatterplot(ax=ax[0],data = aw1,x='actual_price',y='category_2',alpha = 0.3,color = 'red')
sns.scatterplot(ax=ax[1],data = aw1,x = 'discounted_price',y= 'category_2',alpha = 0.3,color = 'orange')
ax[0].set_xlabel('Actual Price (Rupee India)', fontweight='bold')
ax[0].set_ylabel('Product  Sub-Category', fontweight='bold')
ax[0].set_title('Actual Price Range by Product Sub-Category', fontweight='bold')

ax[1].set_xlabel('Discounted Price (Rupee India)', fontweight='bold')
ax[1].set_ylabel('Product Sub-Category', fontweight='bold')
ax[1].set_title('Discounted Price Range by Product Sub-Category', fontweight='bold')

plt.subplots_adjust(hspace = 0.2)
plt.show()

def p25(g):
    return np.percentile(g,25)
def p75(g):
  return np.percentile(g,75)
actual_price_pivot = aw1.pivot_table(values = ['actual_price','discounted_price'],index = ['category_1','category_2'],aggfunc=([p25,np.median,np.mean,p75]))
actual_price_pivot