import pandas as pd
import numpy as np
df=pd.read_csv('IRIS.csv')
#print(df.head)
sepal=df[df['sepal_length']>7]
petal=df[df['petal_length']>6]
species=df['species']
#print(species)
ls=list(species)
ps=[]
js=[]
ms=[]
pk=[]
for i in ls:
    if i == 'Iris-virginica':
        ps.append(i)
    elif i == 'Iris-versicolor':
        js.append(i)
    else:
        ms.append(i)

for i in df['sepal_length']:
    if i >5:
        i=i+1
    else:
        i=None
    pk.append(i)
count=0
new_data=pd.DataFrame({'Data':pk})
#print(new_data)
for i in new_data['Data']:
    if str(i) == 'nan':
        count+=1
'''
#print(new_data.dropna())
#print(new_data.fillna(0))
print(new_data.stack())
print(new_data.unstack())
'''
first=np.random.randint(1,100,20)
second=np.random.randint(1,100,20)
third=np.random.randint(1,100,20)

new=pd.DataFrame({'main':first,'sub-main':second,'header':third})

print(new)