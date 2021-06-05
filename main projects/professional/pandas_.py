import pandas as pd 
s1=pd.Series([1,2,3,4],index=['one','two','three','four'])

'''
print(s1)
print(type(s1))
'''
s2=pd.Series({"i":100,"ii":200,"iii":300,"iv":400,"v":500},index=['v','vi','iv','i','iii','ii'])
#print(s2)

#print(s2[3])
#print(s2[::-1])


l1=[1,2,3,4,5,6,7,8,9]
s3=pd.Series(l1)
'''
print(s3)
print(s3[:4])
print(s3[-5:])
'''

l3=[12,23,34,45,56]
s4=pd.Series(l3)
'''
print(s4+20)
print(s4-20)
print(s4*2)
print(s4/2)
'''

s5=pd.Series([10,20,20,30,40,60,70])
#print(s4+s5)

d1=pd.DataFrame({"name":['lokesh','veera','sharma'],'marks':[80,90,99]})
#print(d1)

d2=pd.read_csv("IRIS.csv")
'''
print(d2)
print(d2.head)
print(d2.tail)
print(d2.shape)
print(d2.describe())
'''

#print(d2.iloc[1:10,0:2])

#print(d2.loc[0:5],('petal.Length'),'Species')
#print(d2.head)
#print(d2.drop('sepal_length',axis=1)) drop by column
#print(d2.drop([1,2,3,4],axis=0))       drop by row

'''
print(d2.mean())
print(d2.median())
print(d2.min())
print(d2.max())
'''

'''
def half(s):
    return s*
print(d2[['sepal_length']].apply(half))
'''

#print(d2['species'].value_counts())
#print(d2.sort_values(by="sepal_length"))