import pandas as pd
import numpy as np
data=pd.read_csv("abalone_dataset.csv")
gh=pd.DataFrame(
{
'A':1,
#'B':pd.Timestamp('20200627'),
'C':pd.Series(2,list(range(4)),dtype='float32'),
'D':np.array([3] * 4,dtype="int32"),
#'E':pd.Categorical(["test", "train", "test", "train"]),
#'F':'foo'
}
)
print(gh [gh['C'] < 0])
print(gh [gh[ 'D'] > 0])

#it doesn't expect timestamp values, catagorical values, string values etc if you remove all comments form upper then upper function work but bottom show error.
print(gh [ gh > 0])