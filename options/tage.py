import pandas as pd
from math import pow, sqrt
movies=pd.read_csv("movies.csv")
tags=pd.read_csv("tags.csv")
tags=pd.merge(movies,tags).drop(['timestamp','movieId','title','genres'],axis=1).sort_values(by=['userId'])
# tags

i=int(input("Enter the user id"))
x=tags.loc[tags['userId'] == i]
# x
t_count = x['tag'].value_counts()
y=t_count[:10]

z=y.index
print("The top 3 tags from the user are")
print(z[0])
print(z[1])
print(z[2])
