# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 15:20:46 2018

@author: jkdadhich
"""
# Moving average List defined suggest in Question
List_a = [3,5,7,2,8,10,11,65,72,81,99,100,150]

moveing_seq = 3 # Number of Sequence
cummlative_sum , moving_average = [0],[] # Define varibale in list form
def Moving_average_fun(List_a, moveing_seq): # Function with two parametter
    N =  moveing_seq # renaming the variable
    for i , j  in enumerate(List_a,1): # Enumeation the variable
        cummlative_sum.append(cummlative_sum[i-1] + j) # appendthe list

        if i>=N: # checking the condition
            moving_ave = round((cummlative_sum[i] - cummlative_sum[i-N])/N,2) #siling the list and summing the round up the value

            #can do stuff with moving_ave here
            moving_average.append(moving_ave) # appending the results
    return (moving_average), len(moving_average) # return the value and length of elements

Result_fun = Moving_average_fun(List_a,moveing_seq)

import pandas as pd # importing Pandas as pd
Data_df =  pd.DataFrame(columns=["List_","Moving_average"]) # Created dataframe with two columns
Data_df["List_"] = List_a # Passing list in pd Series
# Caluating moving average in pandas data frame
Data_df["Moving_average"] = round(Data_df["List_"].rolling(window=moveing_seq).mean(),2)
# Counting the Nan Values
Nan_Values =  int(Data_df["Moving_average"].isnull().sum()) # Counting Nan Values
Data_df = Data_df.dropna() # Droping Nan Values
pandas_mv  =  list(Data_df["Moving_average"]) # Extracting Moving average in list
pandas_seq =  len(Data_df) # Length of Moving average results

print ("~~*~~"*10)
print (" User defined List :-\n {} \n User Define Window Size :-\t {} ".format(List_a,moveing_seq))
print ("~~*~~"*10)
print (" Result Using above defined Funtion :\t")
print (" Moving average value :\n",Result_fun[0])
print (" Moving average seques has :- {}, values".format(Result_fun[1]))
print ("~~@~~"*10)
print (" Result Using Pandas :\t")
print (" Moving average value :\n",pandas_mv)
print (" Moving average seques has :- {}, values".format(pandas_seq))
print ("~~*~~"*10)



