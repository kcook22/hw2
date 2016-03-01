"""
Kerry Cook uni: ksc2138
Columbia W4111 Intro to databases
Homework 2
"""

import sys
from collections import *
from operator import itemgetter

def load_data(file_path):
  """
  This method reads the dataset, and returns a list of rows.
  Each row is a list containing the values in each column.
  """
  import csv
  with file(file_path) as f:
    dialect = csv.Sniffer().sniff(f.read(2048))
    f.seek(0)
    reader = csv.reader(f, dialect)
    return [l for l in reader]


def q1(data):
  """
  @param data the output of load_data()
  @return the number of  distinct types of items (by `description` attribute) in this dataset
  """
  # Try using set for this question (https://docs.python.org/2/tutorial/datastructures.html)
  items_distinct = set() 
  #adds all items to a set which is distinct objects 
  for x in range( 1, len(data)-1): 
  	items_distinct.add(data[x][15])
  #length of set is number of distinct items 
  return len(items_distinct) 

def q2(data):
  """
  @param data the output of load_data()
  @return the number of  distinct `vendor`s (by exact string comparison) in this dataset
  """
  # Try using set for this question (https://docs.python.org/2/tutorial/datastructures.html)
	#same logic as q1 - all items is the set are distinct vendors
  vendors_distinct = set() 
  for x in range (1, len(data) -1):
	vendors_distinct.add(data[x][13]) 
  return len(vendors_distinct) 

def q3(data):
  """
  @param data the output of load_data()
  @return the value of the `store` attribute (the id) of the store that had the most sales (as defined by bottle qty)
  """
  # Try using dictionaries for this question, and make use of the sorted function available for list and dictionaries
  # https://docs.python.org/2/tutorial/datastructures.html
	#makes a dictionary with the store as the key index 
  store_dictionary = {}   
  for x in range ( 1 , len(data) -1):
	sale_qty= int(data[x][20]) 
	#checks if the store index already exists in dictionary 
	if data[x][2] in store_dictionary:
		new_qty = sale_qty + store_dictionary[data[x][2]]
		store_dictionary[data[x][2]] = new_qty
	#else just adds the number into dictionary using store key 
	else: 
		store_dictionary[data[x][2]] = sale_qty
  #find max qty in dictionary and return the store name 
  max_qty = max(store_dictionary.iteritems(), key = itemgetter(1)) 
  return int(max_qty[0]) 

def q4(data):
  """
  @param data the output of load_data()
  @return The value of the `description` attribute of the most sold item from the store from q3()
  """
  # Try using dictionaries for this question, and make use of the sorted function available for list and dictionaries
  # https://docs.python.org/2/tutorial/datastructures.html

  max_store= q3(data) 
  bottle_dictionary = {} 

  #searches for items bought at max store and adds to dictionary 
  for x in range( 1, len(data) -1): 
	if int(data[x][2]) == max_store: 
		if data[x][15] in bottle_dictionary:
			new = bottle_dictionary[data[x][15]] + int(data[x][20]) 
			bottle_dictionary[data[x][15]]=new
		#else just add the number into the dictionary 
		else:
			bottle_dictionary[data[x][15]] = int(data[x][20])
  #find the max item in the dictionary which will be the max item sold 
  max_sold= max(bottle_dictionary.iteritems(), key = itemgetter(1)) 
  return max_sold[0]

def q5(data):
  """
  Finds the `zipcode` that has the greatest total `bottle_qty` for `category_name` "TEQUILA"
  @param data the output of load_data()
  @return The value of the `zipcode` attribute with the most sales in "TEQUILA" category
  """
  # Try using dictionaries for this question, and make use of the sorted function available for list and dictionaries
  # https://docs.python.org/2/tutorial/datastructures.html
  zipCode = {}
  #find all tequilla bottles and add qtys to the dictionary using zip code as key 
  for x in range (1, len(data) -1):
	if data[x][11] =="TEQUILA": 
		if data[x][6] in zipCode: 
			new_count = zipCode[data[x][6]] + int(data[x][20]) 
			zipCode[data[x][6]] = new_count
		else:
			zipCode[data[x][6]] = int(data[x][20]) 
  #find max bottle count of tequila in dictionary and return the zip code
  max_teq = max(zipCode.iteritems(), key = itemgetter(1))
  return int(max_teq[0]) 
 

if __name__ == '__main__':
  if len(sys.argv) != 2:
    sys.stderr.write("Usage: python hw2.py (path to input csv)\n")
    sys.exit(1)
  file_path = sys.argv[1]

  data = load_data(file_path)
  print q1(data)
  print q2(data)
  print q3(data)
  print q4(data)
  print q5(data)
