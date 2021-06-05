import pandas as pd
import numpy as np
data=pd.read_csv("abalone_dataset.csv")
sd=pd.Series([1,2,3,np.nan,5,2,9])
print(sd)
