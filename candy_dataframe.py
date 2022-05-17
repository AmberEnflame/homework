import pandas as pd

Candy = ['bubble gum','chocolate','taffy']
Name = ['Robert', 'Natalie', 'Gia']

data = {'Name': Name, 'Candy': Candy}

df = pd.DataFrame(data=data)
print(df)
