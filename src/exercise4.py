
# coding: utf-8

# # Match searches with bookings

# In[1]:

import pandas as pd
# Load data from csv file
chunksize = 10 ** 6
path = "../data/searches.csv"
delim = "^"

chunks_s = pd.read_csv(path, chunksize = chunksize, sep = delim, header = 0,
                       parse_dates = ['Date'],
                       usecols = ['Date', 'Origin', 'Destination', 'OfficeID'])
searches = pd.DataFrame()
searches = pd.concat(chunks_s)


# In[2]:

path_b = "../data/bookings.csv"
chunks_b = pd.read_csv(path_b, chunksize = chunksize, sep = delim, header = 0,
                         parse_dates = ['act_date           '],
                         usecols = ['act_date           ', 'dep_port', 'arr_port', 'pos_oid  '])
bookings = pd.DataFrame()
bookings = pd.concat(chunks_b)


# In[3]:

# print data
print searches[:5]
print bookings[:5]


# In[4]:

# primary data processing (remove whitespaces in headers and values, rename headers)
# secondary data processing (rename columns in bookings in order to fit the same names in searches)
bookings.rename(columns={'act_date           ' : 'Date', 'dep_port' : 'Origin',
                         'arr_port' : 'Destination', 'pos_oid  ' : 'OfficeID'}, inplace = True)
bookings["OfficeID"] = bookings["OfficeID"].map(str.strip)
bookings["Origin"] = bookings["Origin"].map(str.strip)
bookings["Destination"] = bookings["Destination"].map(str.strip)
# secondary data processing (extract only date)
bookings['Date'] = bookings["Date"].astype(str)
searches['Date'] = searches["Date"].astype(str)
bookings['Date'] = bookings.apply(lambda row: row['Date'][:10], axis=1)
searches['Date'] = searches.apply(lambda row: row['Date'][:10], axis=1)


# In[5]:

# create a column called booked and assign 1 to it
bookings['booked'] = 1 
bookings[:5]


# In[6]:

# left join two tables 'searches' and 'bookings'
result = pd.merge(searches, bookings, how = 'left', on = [ 'Origin', 'Destination', 'OfficeID', 'Date'])

result


# In[11]:

# replace NAN in the column 'booked' by 0
result['booked'].fillna(0, inplace=True)
result[:5]


# In[8]:

# display some booked searches
result.loc[result['booked'] == 1][:5]


# In[12]:

## write to a csv file
result.to_csv('../data/searches_new.csv', sep = "^", index = False, encoding = "utf-8")


# In[13]:

result

