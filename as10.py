import pandas as pd

Books = {'Name': ['The Hobbit', 'Twilight', 'Jane Eyre', 'Animal Farm','The Kite Runner','Life of Pi','Eclipse','The Book Thief','The Giver','The Iliad'],
        'Author':['J. R. R. Tolkien','Stephenie Meyer','Charlotte Brontë','Animal Farm','Khaled Hosseini','Yann Martel','Stephenie Meyer','Markus Zusak ','Lois Lowry ',' Homer']}

df = pd.DataFrame(Books)
print(df)

d=df.describe()

s=input("enter a string to search\n")
print(df[df['Name'].str.contains(s)])