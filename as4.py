import pandas as pd

University = {'Name': ['Ross', 'anita', 'Krish', 'jack','mary','alice','bob','kavya','joey','Jill'],
              'Usn':[101,102,103,104,105,106,107,108,109,110],
              'Sem': [6, 7, 5, 3, 1, 5, 4, 8, 6, 7],
              'Branch':['CSE','ISE','MECH','EEE','ECE','CSE','ISE','ISE','CIV','ECE'],
              'Score':[58,95,65,85,45,32,78,65,75,49],
              'Region':['Belgaum','Mysore','Kalburgi','Bangalore','Belgaum','Mysore','Bangalore','Mysore','Belgaum','Bangalore']}

df = pd.DataFrame(University)
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

print(df.rename(index={0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j'}))
