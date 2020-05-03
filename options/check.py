import pandas as pd
ratings=pd.read_csv("ratings.csv")
movies=pd.read_csv("movies.csv")
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


#action_lover=[("10 Things I Hate About You (1999)",5),("¡Three Amigos! (1986)",1),("Zoolander (2001)",1)]
x=input("Enter the name of your movie")
y=input("Enter the ratings")

# similar_movies=pd.DataFrame()
# for movie,rating in action_lover:
#   similar_movies=similar_movies.append(get_similar_movies(movie,rating),ignore_index=True)
# similar_movies.head()
# similar_movies.sum().sort_values(ascending=False)

similar_movies=pd.DataFrame()
similar_movies=similar_movies.append(get_similar_movies(x,float(y)),ignore_index=True)
print("The top 5 movies are ")
# similar_movies.head(5)
# similar_movies.sum().sort_values(ascending=False).head(5)

similar_movies=similar_movies.sum().sort_values(ascending=False).head(5)
print(similar_movies)