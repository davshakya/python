
import pandas as pd
# s=pd.Series([1,2,3,4,5])
# s=pd.Series([1,2,3,4],index=["a","b","c","d"],dtype=float,name="data values")
# print(s)
# s=pd.Series(0.5,[1,2,3,4])
# s=pd.Series({"a":1,"b":4})
# print(s)

# lst=[1,2,3,4]
# lst=[[1,2,3,4],[6,7,8,9],[5,4,3,3]]
# dc={"a":[1,1,2],"b":[5,6,7]}
# dc={"a":[1],"b":[1]}
# df=pd.DataFrame(lst)

# lst1=[{"a":4,"b":5},{"a":3,"b":7}]
# dc={"s":[11,21,34,5],"k":[9,8,7,1]}
# df=pd.DataFrame(dc)
# print(df)

# cs=pd.read_csv('F:\\Computer_Programmes\\python\\panda.csv')
# print(cs)
 
# cs=pd.read_csv("c:\\panda.csv",nrows=1)
# print(cs)
# print(cs.columns)

# cs=pd.read_csv("c:\\panda.csv", usecols=[1])
# print(cs)
# cs=pd.read_csv("c:\\panda.csv", usecols=[1,4,3])
# print(cs)


# cs=pd.read_csv("c:\\panda.csv", skiprows=[0])
# print(cs)

# cs=pd.read_csv("c:\\panda.csv", skiprows=[0,3])
# print(cs)

# cs=pd.read_csv("c:\\panda.csv",header=None, prefix="Col")
# print(cs)

# cs=pd.read_csv("c:\\panda.csv",names=["a","b","c","e","f"])
# print(cs)


# cs=pd.read_csv("c:\\panda.csv")
# print(cs.head())
# print(cs.head(1))
# print(cs.tail())
# print(cs.tail(1))


# cs=pd.read_csv("c:\\panda.csv",dtype={"Class":"float64"})
# print(cs)



# cs=pd.read_csv("panda1.csv",true_values=["Yes"])
# print(cs)

# cs=pd.read_csv("panda1.csv",na_values={"Admission":"Yes"})
# print(cs)

# cs=pd.read_csv("panda1.csv",na_values={"Admission":"Yes"})
# print(cs.isnull().sum())


# cs=pd.read_csv("panda1.csv",na_values={"Admission":"Yes"})
# # print(cs.notnull().sum())
# print(cs.notnull().sum().sum())

# cs=pd.read_csv("panda1.csv",na_values={"Admission":"Yes"})
# print(cs)
# print(cs.dropna())
# print(cs.dropna(axis=0))

df=pd.read_csv("panda1.csv")
# print(df)
# print(cs.fillna(0))
# print(cs.fillna(3))
# print(cs.replace(to_replace="Jalaun", value="Noida" ))
# print(cs.interpolate())
# print(cs.interpolate(limit_area="inside"))
# print(cs.interpolate(limit_area="outside"))
# print(df.loc[0])
print(df.loc[3  ,"City"])



 