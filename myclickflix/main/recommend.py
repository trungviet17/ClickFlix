import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from main.models import Movie


def get_movie_data():
    movies = Movie.objects.all()[:1000].values("id", "title", "overview", "keyword")
    return pd.DataFrame(movies)


# converting list of string to list (eg. "["abc","def"]" to ["abc","def"])
def convert_to_list(my_list):
    my_list = my_list.split('","')
    my_list[0] = my_list[0].replace('["', "")
    my_list[-1] = my_list[-1].replace('"]', "")
    return my_list


def create_similarity(features):
    features = pd.DataFrame(features)
    # creating a count matrix
    cv = CountVectorizer()
    features["all"] = features["title"] + features["overview"] + features["keyword"]
    count_matrix = cv.fit_transform(features["all"])
    # creating a similarity score matrix
    similarity = cosine_similarity(count_matrix)
    return similarity


def recommend(id, num_suggestion=10):
    movies_data = get_movie_data()
    similarity = create_similarity(movies_data)
    index = movies_data.loc[movies_data["id"] == id]
    if index.empty:
        return []
    index = index.index[0]
    lst = list(enumerate(similarity[index]))
    lst = sorted(lst, key=lambda x: x[1], reverse=True)
    lst = lst[1 : num_suggestion + 1]
    suggestions = []
    for i in range(len(lst)):
        a = lst[i][0]
        suggestions.append(movies_data["id"][a])
    return suggestions
