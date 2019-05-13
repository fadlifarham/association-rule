# %%

import numpy as np  
import matplotlib.pyplot as plt  
import pandas as pd  
from apyori import apriori  
import math

#membaca file
datafile = pd.read_csv("data/dataset2.csv", index_col=False, squeeze=True)
#print(datafile)

print(datafile.head())
# print(datafile.dropna())

#use apriori
records = []  
for i in range(0, 5):
    temp = []
    for j in range(0, 4):
        if str(datafile.values[i, j]) != 'nan':
            temp.append(str(datafile.values[i, j]))
    records.append(temp)

print(records)

#applying apriori
association_rules = apriori(records, min_support=0.3, min_confidence=0.8, use_colnames=True, min_len=2)
association_results = list(association_rules) 
# print(association_results[0])

for item in association_results:
    # print(item)
    #print(item[0])
    # print(item[1])
    # print(len(item[0]))

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    if (len(pair) == 1):
        print("Rule: " + items[0])
    elif (len(pair) == 2):    
        print("Rule: " + items[0] + " -> " + items[1])
    elif (len(pair) == 3):
        print("Rule: " + items[0] + " -> " + items[1] + " & " + items[2]) 

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")