#!/usr/bin/env python
# coding: utf-8

# ## Data Extraction Notebook
# 
# New notebook

# # Data Sources

# ## City of New York Open Data
# ### Filming Locations (Scenes of the City)
# Main source link: https://opendata.cityofnewyork.us
# 
# Datasets to use
# - **Filming Locations (Scenes of the City)**: List of filming locations mentioned in the book Scenes from the City
#     - https://data.cityofnewyork.us/Business/Filming-Locations-Scenes-from-the-City-/qb3k-n8mm/about_data
#     - https://data.cityofnewyork.us/download/qb3k-n8mm/application%2Fxml
# 
# ### IMDb Non-Commercial Datasets
# Main source links
# - https://developer.imdb.com/non-commercial-datasets/
# - https://datasets.imdbws.com
# 
# Datasets to use
# - **name.basics.tsv.gz**
#     - https://datasets.imdbws.com/name.basics.tsv.gz
# - **title.basics.tsv.gz**
#     - https://datasets.imdbws.com/title.basics.tsv.gz
# - **title.ratings.tsv.gz**
#     - https://datasets.imdbws.com/title.ratings.tsv.gz
# 
# General data model connections
# - Bronze and Silver
#     - May not be able to connect between NYC Open Data and IMDb in Bronze because the NYC data's IMDb id is nested in a URL (but definitely will be able to in the Silver layer)
#     - Connect IMDb title ids together between all three datasets in Silver
# - Gold
#     - Only keep needed fields
#     - One big table with each film, location(s), and ratings
# 

# ### Resources
# - Fixing the pivoting error in Power Query: had to create individual row identifiers so Power Query understood how to pivot the data into each of their rows
#     - https://www.youtube.com/watch?v=aTXQ77Vf5Gc

# ### API call from NYC Open Data
# Use Data Extraction Dataflow for this part (the XML got tricky!) See Resources above for what I used to solve the problem

# ### Webscrape from IMDb Non-Commercial Datasets

# In[ ]:


# Import modules
from bs4 import BeautifulSoup
import requests
import io
import os
import pandas as pd
from pyspark.sql import SparkSession
import gzip
import shutil


# In[ ]:


# Initialize variables
name_basics = ''
title_basics = ''
title_ratings = ''


# In[ ]:


# Make soup for web page
response = requests.get(
    'https://datasets.imdbws.com/')
wp = response.text
soup = BeautifulSoup(wp, 'html.parser')


# In[ ]:


# Narrow down to the <a> tags, and grab the .gz download links for needed datasets
links = soup.findAll('a')

for l in links:
    if 'name.basics.tsv.gz' in l.text:
        name_basics = l['href']
    elif 'title.basics.tsv.gz' in l.text:
        title_basics = l['href']
    elif 'title.ratings.tsv.gz' in l.text:
        title_ratings = l['href']


# In[ ]:


# Unzip files from .gz

# name_basics
download_gz_name_basics = requests.get(name_basics, stream=True)
download_gz_name_basics.raise_for_status()
with gzip.GzipFile(fileobj=download_gz_name_basics.raw, mode='rb') as compressed_file:
    with open('name_basics.tsv', 'wb') as outfile:
        shutil.copyfileobj(compressed_file, outfile)

# title_basics
download_gz_title_basics = requests.get(title_basics, stream=True)
download_gz_title_basics.raise_for_status()
with gzip.GzipFile(fileobj=download_gz_title_basics.raw, mode='rb') as compressed_file:
    with open('title_basics.tsv', 'wb') as outfile:
        shutil.copyfileobj(compressed_file, outfile)

# title_ratings
download_gz_title_ratings = requests.get(title_ratings, stream=True)
download_gz_title_ratings.raise_for_status()
with gzip.GzipFile(fileobj=download_gz_title_ratings.raw, mode='rb') as compressed_file:
    with open('title_ratings.tsv', 'wb') as outfile:
        shutil.copyfileobj(compressed_file, outfile)


# In[ ]:


# See extracted files in the main directory
os.listdir()


# In[ ]:


# Initialize Spark session
spark = SparkSession.builder.appName("SaveAsDeltaTable").getOrCreate()


# In[ ]:


# Lakehouse_Main general Delta table path
general_delta_table_path = 'abfss://fdfb449d-34e5-4f41-a2d5-422bde25710f@onelake.dfs.fabric.microsoft.com/57342e7a-f7a7-471a-a0cc-c5ac9a0d66f1/Tables/'

# Add dataframes for each dataset
df__name_basics = pd.read_csv('name_basics.tsv', sep='\t')
df__title_basics = pd.read_csv('title_basics.tsv', sep='\t')
df__title_ratings = pd.read_csv('title_ratings.tsv', sep='\t')

# Convert pandas dataframes to Spark dataframes
spark_df__name_basics = spark.createDataFrame(df__name_basics)
spark_df__title_basics = spark.createDataFrame(df__title_basics)
spark_df__title_ratings = spark.createDataFrame(df__title_ratings)

# Save the Spark dataframes as Delta tables

# For initial load into Lakehouse_Main (comment out when done)
# spark_df__name_basics.write.format("delta").save(general_delta_table_path + '/raw__name_basics')
# spark_df__title_basics.write.format("delta").save(general_delta_table_path + '/raw__title_basics')
# spark_df__title_ratings.write.format("delta").save(general_delta_table_path + '/raw__title_ratings')

# For subsequent loads into Lakehouse_Main
spark_df__name_basics.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(general_delta_table_path + '/raw__name_basics')
spark_df__title_basics.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(general_delta_table_path + '/raw__title_basics')
spark_df__title_ratings.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(general_delta_table_path + '/raw__title_ratings')

