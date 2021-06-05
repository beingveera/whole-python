import pandas as pd
import numpy as np
data=pd.read_csv("abalone_dataset.csv")
gh=pd.DataFrame(
{
'A':1,
'B':pd.date_range('20200627', periods= 4),
'C':pd.Series(2,list(range(4)),dtype='float32'),
'D':np.array([3] * 4,dtype="int32"),
'E':pd.Categorical(["test", "train", "test", "train"]),
'F':'foo'
}
)
#print(gh)
print(gh.sort_index(axis=1,ascending=False))
print(gh.sort_values(by='B'))