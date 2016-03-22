import pandas as pd

df = pd.read_csv("exercise1.csv")
print df
#Notice the row of NaNs - we'll remove that first
df.columns = ["integers1","integers2","text","boolean","throw away"]
df.drop("throw away",axis=2,inplace=True)
print df
#As you can see now the NaN column is gone!  So what did we do to make that happen?  Well, we referrenced the column that we wanted to delete and then we passed in some options.  Specification axis=1 and inplace=True.
#the concept of an axis is a deep concept in pandas.  This stack overflow gives a detailed answer of how you should think about this parameter: http://stackoverflow.com/questions/22149584/what-does-axis-in-pandas-mean
#the short answer is axis=1 means to manipulate across the columns
#next let's look at inplace.  This simply means you don't need to write a new dataframe.  Like python dictionaries, pandas dataframes won't take in changes unless you explicitly tell them to.

#so,

#
#df.append({"a":"some data"})

