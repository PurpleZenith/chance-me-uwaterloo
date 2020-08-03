import os
import pandas as pd


# get filepath and create dataframe
filepath = os.path.abspath(__file__)
filepath = filepath[:-7] + "dataset.csv"
df = pd.read_csv (filepath)

# returns the total number of programs
def programCount ():
    programCount = len(df.columns)
    return programCount
# print(programCount())

# returns the list of programs 
def programList():
    return list (df.columns.values)


# returns the number of nonzero entries the specified column
def nonZeroCount(columnNum):
    columnCountList = list(df.fillna(0).astype(bool).sum(axis=0))
    return columnCountList[columnNum]

# print (programList())


# this method returns the column of data and u give the columnNum
def returnData(columnNum):
    progList = programList()
    programChosen = progList[columnNum]
    df_out = df[programChosen]
    df2 = df_out.truncate (before = 0, after = nonZeroCount(columnNum)-1)
    return df2

