# [CODE] Using Python to Extract a Subset from LFS Microdata Files
Python code that demonstrates how to extract a subset of data that matches a particular condition from Labour Force Survey microdata (PUMF). 

## Problem
The LFS microdata is available as monthly datasets which are then compiled into annual zip files that collect the monthly files together. It can be tedious to manually open and extract relevant rows to build a new spreadsheet/csv file. 
If the search spans several years, this can quickly become a very time-consuming process.

## Solution
Using Python with the pandas and zipfile packages, we can automate this process and quickly put together a dataset that only contains the rows that match the criteria we are seeking.

## What it Does
- Reads a given year span of microdata zipped files and parses just the monthly dataset .csv files within
- Builds a new dataframe using just the rows that match a given criteria
- Saves the dataframe as a new .csv file

## Dependencies
- Python 3+
- pandas
- zipfile

## Included Files
- [Jupyter Notebook](LFS_Dataset_Extraction.ipynb)
- [Python](lfs_microdata_extract.py)

## Data Source
Labour Force Survey (StatsCanada) - [https://www150.statcan.gc.ca/n1/pub/71m0001x/71m0001x2021001-eng.htm](https://www150.statcan.gc.ca/n1/pub/71m0001x/71m0001x2021001-eng.htm)
