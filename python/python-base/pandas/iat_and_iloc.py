import pandas as pd
import numpy as np
data=pd.read_csv("abalone_dataset.csv")
gh=pd.DataFrame(
{
'A':1,
'B':pd.Timestamp('20200627'),
'C':pd.Series(2,list(range(4)),dtype='float32'),
'D':np.array([3] * 4,dtype="int32"),
'E':pd.Categorical(["test", "train", "test", "train"]),
'F':'foo'
}
)
print(gh.iat[2,2])
print(gh.iloc[1,1])
