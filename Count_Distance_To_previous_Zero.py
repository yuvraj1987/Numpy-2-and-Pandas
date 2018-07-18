# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 17:44:11 2018

@author: jkdadhich
"""
import pandas as pd # Importing pandas as pd
df_1 = pd.DataFrame(({'X':[7,2,0,3,4,2,5,0,3,4,0,4,]})) # Suggest input elements
start_with = 0 # Setting Count as Zero to rest
def up_date_zero(x): # Created funtion to obtain results
    global start_with # Declare variable for function use
    if x==0: # Value Equal to Zero setting global value to Zero
        start_with = 0
    elif x !=0: # if value not equal to zero than adding counter
        start_with = start_with +1
    return start_with # return the counter value
df_1["Y"] = [ up_date_zero(x) for x in df_1["X"]] # Updating value in Dataframe column "Y"


df = pd.DataFrame(({'X':[7,2,0,3,4,2,5,0,3,4,0,4,5]})) # Suggest input
# using pandas inbuilt function cummulative sum and masking check with Zero return to "Y"
df["Y"] = (df.X.groupby(df.X.eq(0).cumsum().mask(df.X.eq(0))).cumcount() + 1).mask(df.X.eq(0), 0).tolist()
#
List_a =[7,2,0,3,4,2,5,0,3,4,0,4,5] # List For the same task declare
# List comphershion , used to obtain result not store in data frame
Index_ = [(List_a[i::-1]+[0]).index(0) for i in range(len(List_a))]

print ("Desired Out put Values")
print ("~~*~~"*10)
print ("Using Pandas Function out put :-\n",df)
print ("~~*~~"*10)
print ("Using Created Function out put :-\n",df_1)
print ("~~*~~"*10)
print ("Using List Comphershion out put :-\n",Index_)
print ("~~*~~"*10)







































