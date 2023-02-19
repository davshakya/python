import pandas as pd
import numpy as np

dict1={"city":["kanpur","Agra0","Delhi","Lucknow"],"Age":[36,39,40,34], "Name":["Vikas","Navin","Ravi","Dharam"]}
df=pd.DataFrame(dict1)
print(df) 
df.to_csv("csv_file.csv")

df.to_csv("csv_file_false.csv",index=False)


