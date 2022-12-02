import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

df = pd.read_csv('books.csv')
df.insert(0, 'index', range(0, df.shape[0]))
df["Title"] = df.Title.str.replace(', The', '')
df["Title"] = df.Title.str.replace(', A', '')
df['Genre'] = df['Genre'].str.replace('signal_processing', 'signalprocessing')
df['Genre'] = df['Genre'].str.replace('data_science', 'datascience')
df['Genre'] = df['Genre'].str.replace('computer_science', 'computerscience')

def get_title_index_from_genre(genre):
    return df[df.Genre == genre].index.values[0]

def get_title_from_genre_index(i):
    return df[df.index == i].Title.values[0]

def contents_based_recommender(n,m):
    results_list = []
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['Genre'])
    sim_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)
    title_index = get_title_index_from_genre(n)
    books_list = list(enumerate(sim_matrix[int(title_index)]))
    similar_books = list(filter(lambda x:x[0] != int(title_index), sorted(books_list,key=lambda x:x[1], reverse=True)))
    for i,s in similar_books[:m]:
        results_list.append(get_title_from_genre_index(i))

    return results_list




