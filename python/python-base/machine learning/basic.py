import numpy as np
import pandas as pd
data={"roll_no":[1,2,3,5,7,3],
"Status":['yes','no','yes',"no",'yes','yes']
}
op=[1,2,3,4,5,6]
df=pd.DataFrame(data,index=op)
#print(df)
print(df["Status"].describe)