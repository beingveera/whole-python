import pandas as pd
import numpy as np
data=pd.read_csv("abalone_dataset.csv")
bn=pd.date_range('20200627',periods=10,freq='D')
#freq= Y,M,N,D
print(bn)

