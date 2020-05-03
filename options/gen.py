import pandas as pd
from math import pow, sqrt
ratings=pd.read_csv("ratings.csv")
movies=pd.read_csv("movies.csv")
ratings=pd.merge(movies,ratings).drop(['timestamp','movieId','title','rating'],axis=1).sort_values(by=['userId'])

i=int(input("Enter the user id"))
x=ratings.loc[ratings['userId'] == i]
# x

gen_count = x['genres'].value_counts()
y=gen_count[:10]

print(y)

z=y.index
z[0]
txt=z[0]
t=txt.split("|")
print(t)
# gen_count[:10].plot(kind = 'bar', figsize=(10,5) )