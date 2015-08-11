
# coding: utf-8

# # find out the top 10 arrival airports in the world in 2013 (using the bookings file)

# In[ ]:

import pandas as pd

def get_top_arrival_airports(path, delim, nbAirport):
    """
    This functions looks for top 10 arrival airports in the world in a certain year
    
    Args:
        path(String): path where the csv file is stored
        delim(String): deliminator
        nbAirport(int): number of top arrival airports
    Returns:
        pax_count(int): number indicates the number of lines for a csv file
    """
    chunksize = 10 ** 6

    chunks = pd.read_table(path, chunksize=chunksize, sep=delim, header=0, usecols = ['arr_port', 'pax'])
    df = pd.DataFrame()
    df = pd.concat(chunks, ignore_index=True)
    pax_count = chunk.groupby('arr_port').aggregate(sum)
    pax_count = pax_count.sort(columns=['pax'], ascending = False)
    return pax_count[0:nbAirport]

top_10_arrival_airports = get_top_arrival_airports("../data/bookings.csv", "^", 10)
print top_10_arrival_airports

