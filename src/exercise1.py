
# coding: utf-8

# # Count the number of lines in Python for each file

# In[31]:

import csv

def count_lines(path, delim):
    """
    This functions counts the number of lines for a csv file (we assume that the first line is header)
    
    Args:
        path(String): path where the csv file is stored
        delim(String): deliminator
    Returns:
        line_count(int): number indicates the number of lines for a csv file
    """
    f = open(path, 'rb')
    raw_data = csv.reader(f, delimiter=delim)
    header = raw_data.next()
    line_count = sum(1 for row in raw_data)
    f.close()
    return line_count

nb_lines_b = count_lines('../data/bookings.csv', "^")
nb_lines_s = count_lines('../data/searches.csv', "^")

print "Number of lines in bookings.csv: " + str(nb_lines_b)
print "Number of lines in searches.csv: " + str(nb_lines_s)


