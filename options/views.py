from django.shortcuts import render
# from .models import movie
import pandas as pd
import os
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
from math import pow, sqrt

def home(request):
    return render(request,'first.html')
def opt(request):

    ratings=pd.read_csv("C:\\Users\\sonuy\\OneDrive\\Desktop\\TSEC\\movrec\\options\\ratings.csv")
    movies=pd.read_csv("C:\\Users\\sonuy\\OneDrive\\Desktop\\TSEC\\movrec\\options\\movies.csv")
#movies.head(4)
    ratings=pd.merge(movies,ratings).drop(['genres','timestamp'],axis=1)
#ratings.head(4)
    user_ratings=ratings.pivot_table(index=['userId'],columns=['title'],values='rating')
#user_ratings.head(3)
    print("**************************yes**********************")
    user_ratings=user_ratings.dropna(thresh=10,axis=1).fillna(0)

    item_similarity_df=user_ratings.corr(method='pearson')


    def get_similar_movies(movie_name,user_rating):
        similar_score=item_similarity_df[movie_name]*(user_rating-2.5)
        similar_score=similar_score.sort_values(ascending=False)
        return similar_score

    x=request.POST['name']
    # y=request.POST['rat']
    y="5"

    similar_movies=pd.DataFrame()
    similar_movies=similar_movies.append(get_similar_movies(x,float(y)),ignore_index=True)
    print("The top 5 movies are ")

    similar_movies=similar_movies.sum().sort_values(ascending=False).head(5)
    
    print(similar_movies)
   
    x1=list(similar_movies.index)
    y1=similar_movies[0:].tolist()
    # print(name)
    send=zip(x1,y1)
    return render(request,'op3.html',{'movie':x,'rate':y,'send':send})

def movie(request):
    return render(request,'options.html')

def user(request):
    return render(request,'user.html')

def show(request):
    ratings=pd.read_csv("C:\\Users\\sonuy\\OneDrive\\Desktop\\TSEC\\movrec\\options\\ratings.csv",index_col=0)
    ratings=ratings.fillna(0) #logically can't assign 0 rating as user haven't seen it yet ratings

    user_ratings=ratings.pivot_table(index=['userId'],columns=['movieId'],values='rating')
# user_ratings.head(3)

    user_ratings=user_ratings.dropna(thresh=10,axis=1).fillna(0)
# user_ratings.head(442)

    def standardize(row):
        new_row=(row-row.mean())/(row.max()-row.min())
        return new_row

    ratings_std=user_ratings.apply(standardize)
    ratings_std=ratings_std.T
# ratings_std

    item_similarity=cosine_similarity(ratings_std.T)
# print(item_similarity)

# len1=len(ratings_std.index)
    item_similarity_df=pd.DataFrame(item_similarity,index=ratings_std.columns,columns=ratings_std.columns)
# item_similarity_df.head(313)
    def get_similar_user(user_Id):
        similar_score=item_similarity_df[user_Id]
        similar_score=similar_score.sort_values(ascending=False)#sorting in dec order
        return similar_score

    x=request.POST['ident']
    print(x)
    print("The other users similar to you are")
    y=get_similar_user(int(x)).head(5)
    x1=list(y.index)
    y1=y[0:].tolist()
    print(x1)
    print(y1)
    print(y)
    
    send=zip(x1,y1)
    return render(request,'op4.html',{'send':send,'x':x})



def genere(request):
    return render(request,'gen.html')

def genfinal(request):
    ratings=pd.read_csv("C:\\Users\\sonuy\\OneDrive\\Desktop\\TSEC\\movrec\\options\\ratings.csv")
    movies=pd.read_csv("C:\\Users\\sonuy\\OneDrive\\Desktop\\TSEC\\movrec\\options\\movies.csv")

    ratings=pd.merge(movies,ratings).drop(['timestamp','movieId','title','rating'],axis=1).sort_values(by=['userId'])

    i=int(request.POST['ident'])
    x=ratings.loc[ratings['userId'] == i]
# x

    gen_count = x['genres'].value_counts()
    y=gen_count[:10]

    print(y)


# gen_count[:10].plot(kind = 'bar', figsize=(10,5) )
    x1=list(y.index)
    y1=y[0:].tolist()
    print(y1)
    print(x1)
    send=zip(x1,y1)
    return render(request,'rend.html',{'send':send})
def sat(request):
    return render(request,'stat.html')
def graprat(request):
    return render(request,'graprat.html')
def graph(request):
    return render(request,'graph.html')
def grapmov(request):
    return render(request,'grapmov.html')
def tot(request):
    return render(request,'tot.html')



def tag(request):
    return render(request,'take.html')


def tag1(request):
    # import pandas as pd

    movies=pd.read_csv("C:\\Users\\sonuy\\OneDrive\\Desktop\\TSEC\\movrec\\options\\movies.csv")
    tags=pd.read_csv("C:\\Users\\sonuy\\OneDrive\\Desktop\\TSEC\\movrec\\options\\tags.csv")
    tags=pd.merge(movies,tags).drop(['timestamp','movieId','title','genres'],axis=1).sort_values(by=['userId'])
# tags

    i=int(request.POST['indent'])
    x=tags.loc[tags['userId'] == i]
# x

    t_count = x['tag'].value_counts()
    y=t_count[:10]

    z=y.index
    print("The top 3 tags from the user are")
    print(z[0])
    print(z[1])
    print(z[2])
    return render(request,'tag.html',{'x':z})