import pandas as pd
import numpy as np
data=pd.read_csv("abalone_dataset.csv")
for I in data.columns:
	print(I)
