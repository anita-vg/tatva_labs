import pandas as pd
df=pd.read_csv("as5.csv")
print(df)

d=df.describe()
print("Description \n",d)

print("the student with maximum marks is ",df['Name'][df['Score']==df['Score'].max()])

x=df.groupby(['Sem']).groups
print("Group by sem \n",x)

r=df.groupby(['Region']).groups
print("Group by region \n",r)

df['Name']=df['Name'].str.capitalize()
print("Capitalized name \n",df['Name'])

df=pd.DataFrame(df,index=['a','b','c','d','e','f','g','h','i'])
print("indexing \n",df)