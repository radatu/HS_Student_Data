#!/usr/bin/env python
# coding: utf-8

# ### Import required dependencies

# In[25]:


import pandas as pd
import os
import numpy as np


# ## Deliverable 1: Collect the Data
# 
# To collect the data that you’ll need, complete the following steps:
# 
# 1. Using the Pandas `read_csv` function and the `os` module, import the data from the `new_full_student_data.csv` file, and create a DataFrame called student_df. 
# 
# 2. Use the head function to confirm that Pandas properly imported the data.
# 

# In[2]:


# Create the path and import the data
full_student_data = os.path.join('Resources/new_full_student_data.csv')
student_df = pd.read_csv(full_student_data)


# In[4]:


# Verify that the data was properly imported
student_df.head(5)
student_df.sample()
# Why do the above not print? Are they overwritten right away? How would I print all three? Is .sample method the best test?
student_df.tail(5)


# In[29]:


print(student_df.head())
student_df["grade"]


# ## Deliverable 2: Prepare the Data
# 
# To prepare and clean your data for analysis, complete the following steps:
#     
# 1. Check for and remove all rows with `NaN`, or missing, values in the student DataFrame. 
# 
# 2. Check for and remove all duplicate rows in the student DataFrame.
# 
# 3. Use the `str.replace` function to remove the "th" from the grade levels in the grade column.
# 
# 4. Check data types using the `dtypes` property.
# 
# 5. Remove the "th" suffix from every value in the grade column using `str` and `replace`.
# 
# 6. Change the grade colum to the `int` type and verify column types.
# 
# 7. Use the head (and/or the tail) function to preview the DataFrame.

# In[5]:


# Check for null values
student_df.isna().sum()


# In[6]:


# Drop rows with null values and verify removal
student_df.dropna(inplace = True)
student_df.isna().sum()


# In[9]:


# Check for duplicated rows
student_df.duplicated()
student_df.duplicated().sum()


# In[16]:


# Drop duplicated rows and verify removal
student_df.drop_duplicates()
student_df.duplicated().sum()


# In[20]:


# Check data types
student_df.duplicated()


# In[29]:





# In[22]:


# Examine the grade column to understand why it is not an int
grade = student_df(2)


# In[31]:


# Remove the non-numeric characters and verify the contents of the column


# In[32]:


# Change the grade column to the int type and verify column types


# ## Deliverable 3: Summarize the Data
# 
# Describe the data using summary statistics on the data as a whole and on individual columns.
# 
# 1. Generate the summary statistics for each DataFrame by using the `describe` function.
# 
# 2. Display the mean math score using the `mean` function. 
# 
# 2. Store the minimum reading score as `min_reading_score`.

# In[33]:


# Display summary statistics for the DataFrame


# In[34]:


# Display the mean math score using the mean function


# In[35]:


# Store the minimum reading score as min_reading_score


# ## Deliverable 4: Drill Down into the Data
# 
# Drill down to specific rows, columns, and subsets of the data.
# 
# To drill down into the data, complete the following steps:
# 
# 1. Use `loc` to display the grade column.
# 
# 2. Use `iloc` to display the first 3 rows and columns 3, 4, and 5.
# 
# 3. Show the rows for grade nine using `loc`.
# 
# 4. Store the row with the minimum overall reading score as `min_reading_row` using `loc` and the `min_reading_score` found in Deliverable 3.
# 
# 5. Find the reading scores for the school and grade from the output of step three using `loc` with multiple conditional statements.
# 
# 6. Using conditional statements and `loc` or `iloc`, find the mean reading score for all students in grades 11 and 12 combined.

# In[36]:


# Use loc to display the grade column


# In[37]:


# Use `iloc` to display the first 3 rows and columns 3, 4, and 5.


# In[38]:


# Select the rows for grade nine and display their summary statistics using `loc` and `describe`.


# In[39]:


# Store the row with the minimum overall reading score as `min_reading_row`
# using `loc` and the `min_reading_score` found in Deliverable 3.


# In[40]:


# Use loc with conditionals to select all reading scores from 10th graders at Dixon High School.


# In[41]:


# Find the mean reading score for all students in grades 11 and 12 combined.


# ## Deliverable 5: Make Comparisons Between District and Charter Schools
# 
# Compare district vs charter schools for budget, size, and scores.
# 
# Make comparisons within your data by completing the following steps:
# 
# 1. Using the `groupby` and `mean` functions, look at the average reading and math scores per school type.
# 
# 1. Using the `groupby` and `count` functions, find the total number of students at each school.
# 
# 2. Using the `groupby` and `mean` functions, find the average budget per grade for each school type.

# In[42]:


# Use groupby and mean to find the average reading and math scores for each school type.


# In[43]:


# Use the `groupby`, `count`, and `sort_values` functions to find the
# total number of students at each school and sort from most students to least students.


# In[ ]:





# # Deliverable 6: Summarize Your Findings
# In the cell below, write a few sentences to describe any discoveries you made while performing your analysis along with any additional analysis you believe would be worthwhile.

# *your summary here*
