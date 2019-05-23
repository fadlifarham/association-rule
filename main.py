# %%

import numpy as np  
import matplotlib.pyplot as plt  
import pandas as pd  
from apyori import apriori  
import math

# MARK -> Read File Dataset
datafile = pd.read_csv("data/apriori.csv", index_col=False, squeeze=True)

# MARK -> Show Dataset
print(datafile.head())

# MARK -> Preprocessing
records = []  
for i in range(0, datafile.shape[0]):
    temp = []
    for j in range(0, datafile.shape[1]):
        if str(datafile.values[i, j]) != 'nan':
            temp.append(str(datafile.values[i, j]))
    records.append(temp)

# MARK -> Do Apriori
association_rules = apriori(records, min_support=0.3, min_confidence=0.8, use_colnames=True, min_len=2)
association_results = list(association_rules)

# MARK -> Show Output
print()
for item in association_results:
    itemset = [x for x in item[0]]
    order_statistics = item[2][0]


    for i in range(0, len(itemset)):
        if i == 0:
            print("Rule :", itemset[i], end=" ")
        else :
            print("->", itemset[i], end=" ")
    print()
    print("Confidence : ", order_statistics.confidence)
    print("=====================")