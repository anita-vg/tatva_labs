import pandas as pd

University = {'Name': ['Ross', 'anita', 'Krish', 'jack','mary','alice','bob','kavya','joey','Jill'],
              'Usn':[101,102,103,104,105,106,107,108,109,110],
              'Sem': [6, 7, 5, 3, 1, 5, 4, 8, 6, 7],
              'Branch':['CSE','ISE','MECH','EEE','ECE','CSE','ISE','ISE','CIV','ECE'],
              'Score':[58,95,65,85,45,32,78,65,75,49],
              'Region':['Belgaum','Mysore','Kalburgi','Bangalore','Belgaum','Mysore','Bangalore','Mysore','Belgaum','Bangalore']}

df = pd.DataFrame(University)
df.to_csv(r'C:\Users\Admin\Desktop\python projects\as7.csv')
