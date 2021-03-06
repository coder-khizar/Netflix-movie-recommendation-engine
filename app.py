import pickle
import streamlit as st
import requests


st.set_page_config(
    page_title="Netflix Movie Recommendation Engine",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_url = []
    recommended_movie_vote_average = []
    recommended_movie_vote_count = []
    recommended_movie_release_date=[]
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_url.append(movies.iloc[i[0]].homepage)
        recommended_movie_vote_average.append(movies.iloc[i[0]].vote_average)
        recommended_movie_vote_count.append(movies.iloc[i[0]].vote_count)
        recommended_movie_release_date.append(movies.iloc[i[0]].release_date.split('-')[0])

    return recommended_movie_names,recommended_movie_posters,recommended_movie_url,recommended_movie_vote_average,recommended_movie_vote_count,recommended_movie_release_date

def top_rated_movie():
    index = new_movies[new_movies['vote_average'] >= 8.1]
    movie_names = []
    movie_posters = []
    movie_vote_average = []
    movie_release_date=[]
    for i in range(6):
        movie_names.append(index.iloc[i].title)
        movie_posters.append(fetch_poster(index.iloc[i].movie_id))
        movie_vote_average.append(index.iloc[i].vote_average)
        movie_release_date.append(index.iloc[i].release_date.split('-')[0])
       
    return movie_names,movie_posters,movie_vote_average,movie_release_date

st.title('Netflix Movie Recommendation Engine')
movies = pickle.load(open('./movie_list.pkl','rb'))
similarity = pickle.load(open('./similarity.pkl','rb'))
new_movies = pickle.load(open('./new_movies.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type here or select a movie name from  dropdown",
    movie_list
)


if st.button('Show Relatecd Movie'):
    recommended_movie_names,recommended_movie_posters,recommended_movie_url,recommended_movie_vote_average,recommended_movie_vote_count,recommended_movie_release_date = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(recommended_movie_posters[0])
        st.subheader(recommended_movie_names[0])
        # with st.expander:
        st.text("Release Year: {}".format(recommended_movie_release_date[0]))
        st.write("Visit official link {}".format(recommended_movie_url[0]))
        
        st.caption("Average Vote : {}".format(recommended_movie_vote_average[0]))
        st.caption("Total Vote : {}".format(recommended_movie_vote_count[0]))
    with col2:
        st.image(recommended_movie_posters[1])
        st.subheader(recommended_movie_names[1])
        st.text("Release Year: {}".format(recommended_movie_release_date[1]))
        st.write("Visit official link {}".format(recommended_movie_url[1]))
        st.caption("Average Vote : {}".format(recommended_movie_vote_average[1]))
        st.caption("Total Vote : {}".format(recommended_movie_vote_count[1]))

    with col3:
        st.image(recommended_movie_posters[2])
        st.subheader(recommended_movie_names[2])
        st.text("Release Year: {}".format(recommended_movie_release_date[2]))
        st.write("Visit official link {}".format(recommended_movie_url[2]))
        st.caption("Average Vote : {}".format(recommended_movie_vote_average[2]))
        st.caption("Total Vote : {}".format(recommended_movie_vote_count[2]))

    with col4:
        st.image(recommended_movie_posters[3])
        st.subheader(recommended_movie_names[3])
        st.text("Release Year: {}".format(recommended_movie_release_date[3]))
        st.write("Visit official link {}".format(recommended_movie_url[3]))
        st.caption("Average Vote : {}".format(recommended_movie_vote_average[3]))
        st.caption("Total Vote : {}".format(recommended_movie_vote_count[3]))

    with col5:
        st.image(recommended_movie_posters[4])
        st.subheader(recommended_movie_names[4])
        st.text("Release Year: {}".format(recommended_movie_release_date[4]))
        st.write("Visit official link {}".format(recommended_movie_url[4]))
        st.caption("Average Vote : {}".format(recommended_movie_vote_average[4]))
        st.caption("Total Vote : {}".format(recommended_movie_vote_count[4]))



st.header('Top Rted Movie')
movie_names,movie_posters,movie_vote_average,movie_release_date = top_rated_movie()
col1, col2, col3, col4, col5 =st.columns(5)

with col1:
    st.image(movie_posters[0])
    st.subheader(movie_names[0])
    st.caption("Average Vote : {}".format(movie_vote_average[0]))
    st.text("Release Year: {}".format(movie_release_date[0]))
with col2:
    st.image(movie_posters[1])
    st.subheader(movie_names[1])
    st.caption("Average Vote : {}".format(movie_vote_average[1]))
    st.text("Release Year: {}".format(movie_release_date[1]))
with col3:
    st.image(movie_posters[2])
    st.subheader(movie_names[2])
    st.caption("Average Vote : {}".format(movie_vote_average[2]))
    st.text("Release Year: {}".format(movie_release_date[2]))
with col4:
    st.image(movie_posters[3])
    st.subheader(movie_names[3])
    st.caption("Average Vote : {}".format(movie_vote_average[3]))
    st.text("Release Year: {}".format(movie_release_date[3]))

with col5:
    st.image(movie_posters[4])
    st.subheader(movie_names[4])
    st.caption("Average Vote : {}".format(movie_vote_average[4]))
    st.text("Release Year: {}".format(movie_release_date[4]))



st.header('Top Crime Movie')
recommended_movie_names,recommended_movie_posters,recommended_movie_url,recommended_movie_vote_average,recommended_movie_vote_count,recommended_movie_release_date = recommend('The Dark Knight Rises')
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image(recommended_movie_posters[0])
    st.subheader(recommended_movie_names[0])
    st.write("Visit official link {}".format(recommended_movie_url[0]))
    st.caption("Average Vote : {}".format(recommended_movie_vote_average[0]))
    st.caption("Total Vote : {}".format(recommended_movie_vote_count[0]))

    with col2:
        st.image(recommended_movie_posters[1])
        st.subheader(recommended_movie_names[1])
        st.write("Visit official link {}".format(recommended_movie_url[1]))
        st.caption("Average Vote : {}".format(recommended_movie_vote_average[1]))
        st.caption("Total Vote : {}".format(recommended_movie_vote_count[1]))


    with col3:
        st.image(recommended_movie_posters[2])
        st.subheader(recommended_movie_names[2])
        st.write("Visit official link {}".format(recommended_movie_url[2]))
        st.caption("Average Vote : {}".format(recommended_movie_vote_average[2]))
        st.caption("Total Vote : {}".format(recommended_movie_vote_count[2]))

    with col4:
        st.image(recommended_movie_posters[3])
        st.subheader(recommended_movie_names[3])
        st.write("Visit official link {}".format(recommended_movie_url[3]))
        st.caption("Average Vote : {}".format(recommended_movie_vote_average[3]))
        st.caption("Total Vote : {}".format(recommended_movie_vote_count[3]))

st.header('Top Action Movie')
recommended_movie_names,recommended_movie_posters,recommended_movie_url,recommended_movie_vote_average,recommended_movie_vote_count,recommended_movie_release_date = recommend('Avatar')
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image(recommended_movie_posters[0])
    st.subheader(recommended_movie_names[0])
    st.write("Visit official link {}".format(recommended_movie_url[0]))
    st.caption("Average Vote : {}".format(recommended_movie_vote_average[0]))
    st.caption("Total Vote : {}".format(recommended_movie_vote_count[0]))

    with col2:
        st.image(recommended_movie_posters[1])
        st.subheader(recommended_movie_names[1])
        st.write("Visit official link {}".format(recommended_movie_url[1]))
        st.caption("Average Vote : {}".format(recommended_movie_vote_average[1]))
        st.caption("Total Vote : {}".format(recommended_movie_vote_count[1]))


    with col3:
        st.image(recommended_movie_posters[2])
        st.subheader(recommended_movie_names[2])
        st.write("Visit official link {}".format(recommended_movie_url[2]))
        st.caption("Average Vote : {}".format(recommended_movie_vote_average[2]))
        st.caption("Total Vote : {}".format(recommended_movie_vote_count[2]))

    with col4:
        st.image(recommended_movie_posters[3])
        st.subheader(recommended_movie_names[3])
        st.write("Visit official link {}".format(recommended_movie_url[3]))
        st.caption("Average Vote : {}".format(recommended_movie_vote_average[3]))
        st.caption("Total Vote : {}".format(recommended_movie_vote_count[3]))

st.header('Top Romance Movie')
recommended_movie_names,recommended_movie_posters,recommended_movie_url,recommended_movie_vote_average,recommended_movie_vote_count,recommended_movie_release_date = recommend('Spider-Man 3')
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image(recommended_movie_posters[0])
    st.subheader(recommended_movie_names[0])
    st.write("Visit official link {}".format(recommended_movie_url[0]))
    st.caption("Average Vote : {}".format(recommended_movie_vote_average[0]))
    st.caption("Total Vote : {}".format(recommended_movie_vote_count[0]))

    with col2:
        st.image(recommended_movie_posters[1])
        st.subheader(recommended_movie_names[1])
        st.write("Visit official link {}".format(recommended_movie_url[1]))
        st.caption("Average Vote : {}".format(recommended_movie_vote_average[1]))
        st.caption("Total Vote : {}".format(recommended_movie_vote_count[1]))


    with col3:
        st.image(recommended_movie_posters[2])
        st.subheader(recommended_movie_names[2])
        st.write("Visit official link {}".format(recommended_movie_url[2]))
        st.caption("Average Vote : {}".format(recommended_movie_vote_average[2]))
        st.caption("Total Vote : {}".format(recommended_movie_vote_count[2]))

    with col4:
        st.image(recommended_movie_posters[3])
        st.subheader(recommended_movie_names[3])
        st.write("Visit official link {}".format(recommended_movie_url[3]))
        st.caption("Average Vote : {}".format(recommended_movie_vote_average[3]))
        st.caption("Total Vote : {}".format(recommended_movie_vote_count[3]))



st.subheader('created by Md Khizar hayat & Debanjana Gupta under guidance of Saurav sir')

