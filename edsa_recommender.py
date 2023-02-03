"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
from PIL import Image

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Solution Overview", "Explore", "About Us", "Contact Us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    # Building "Solution Overview" page
    if page_selection == "Solution Overview":
        st.title("MARCO Recommender")
        st.write("### Solution Overview")
        
        st.info("#### About the App")
        col1, col2 = st.columns(2)
        with col1:
            pic = Image.open("resources/imgs/movies.jpeg")
            st.image(pic)
        with col2:
            st.write("When there are numerous options to choose from, it’s natural to be confused… We’ve got you covered!")
            
            st.write("The MARCO Recommender App stands apart from all other business apps due to its special ability to help you choose by eliminating the options that do not align with your movie preferences or past ratings")
            #st.write("The MARCO Recommender App stands apart from all other business apps due to its special capacity to predict with extreme accuracy how a user would evaluate a movie they have not yet seen based on their past performances.")
        
        st.write("#### Behind the Scene!")
        st.write("Our dynamic app was built on the two main algorithms for recommender systems. They are:")

        if st.checkbox("Content-based filtering"):
            image = Image.open("resources/imgs/content.png")
            image1 = image.resize((350, 400))
            st.image(image1)
        if st.checkbox("Collaborative-based filtering"):
            image = Image.open("resources/imgs/file1.png")
            image2 = image.resize((350, 400))
            st.image(image2)

    # Building the "Explore" page
    if page_selection == "Explore":
        st.title("MARCO Recommender")
        st.write("### Exploratory Data Analysis (EDA)")
        st.markdown("This section contains insights on the loaded dataset and its output")

        option = st.sidebar.selectbox('Select visualization', ('Ratings', 'Genres', 'Release Year', 'Directors', 'Actors', 'Keywords'))
        if option == 'Ratings':
            with st.expander('Top users by number of ratings'):
                image = Image.open('resources/imgs/Users_ratings.PNG')
                st.image(image)
            with st.expander('Distribution of ratings'):
                image = Image.open('resources/imgs/Dist_ratings.PNG')
                st.image(image)
            with st.expander('Distribution of ratings'):
                image = Image.open('resources/imgs/Dist_ratings2.PNG')
                st.image(image)
        elif option == 'Genres':
            with st.expander('Number of movies per genre'):
                image = Image.open('resources/imgs/genre.PNG')
                st.image(image)
            with st.expander('Trends in genre popularity'):
                image = Image.open('resources/imgs/trends_genre.PNG')
                st.image(image)
        elif option == 'Release Year':
            with st.expander('Movies released per year'):
                image = Image.open('resources/imgs/movies_year.PNG')
                st.image(image)
        elif option == 'Directors':
            with st.expander('Wordcloud of movies directors'):
                image = Image.open('resources/imgs/movies_directors.PNG')
                st.image(image)
        elif option == 'Actors':
            with st.expander('Wordcloud of actors'):
                image = Image.open('resources/imgs/actors.PNG')
                st.image(image)
        elif option == 'Keywords':
            with st.expander('Wordcloud of keywords'):
                image = Image.open('resources/imgs/keywords.PNG')
                st.image(image)


    # Building the "About Us" page
    if page_selection == "About Us":
        st.title("MARCO Recommender")
        st.info("MARCO Tech Ltd")
        st.write("MARCO Tech Ltd provides data and analytics services that enable data-driven insights, well-timed and informed decisions that consistently position the company's clents ahead of the curve.")

        st.info("Our Vision")
        st.write("To be the leading global data-driven solutions provider")

        st.info("Meet the Team")
        Akor = Image.open("resources/imgs/official_pic.jpg")
        Akor1 = Akor.resize((150, 155))
        Peter = Image.open("resources/imgs/Peter.jpg")
        Peter1 = Peter.resize((150, 155))
        Nnanna = Image.open("resources/imgs/Peter.jpg")
        Nnanna1 = Nnanna.resize((150, 155))
        Chiamaka = Image.open("resources/imgs/Ann.jpg")
        Chiamaka1 = Chiamaka.resize((150, 155))
        Maryam = Image.open("resources/imgs/Maryam1.jpg")
        Maryam1 = Maryam.resize((150, 155))

        col1, col2, col3 = st.columns(3)
        with col2:
            st.image(Akor1, width=150, caption="Akor Christian: Team Lead")
            
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.image(Chiamaka1, width=150, caption="Ann Chiamaka: Project Manager")
        with col2:
            st.image(Nnanna1, width=150, caption="Nnanna Onwnuneme: Senior Data Scientist")
        with col3:
            st.image(Maryam1, width=150, caption="Maryam Adebukola: Software Engineer")
        with col4:
            st.image(Peter1, width=150, caption="Peter Okeke: Technical Support")


    # Building the "Contact Us" page
    if page_selection == "Contact Us":
        image = Image.open('resources/imgs/Contact_us.jpg')
        image1 = image.resize((1296, 380))
        st.image(image1)
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Contact info")
            st.write("82, Bush Willow Lane")
            st.write("Johannesburg, 2086, South Africa")
            st.write("Telephone:+234 7036172544")
            st.write("WhatsApp:+234 8093224263")
            st.write("Email: info@marcotech.com")
        with col2:
            st.subheader("Send Us")
            email = st.text_input("Enter your email")
            message = st.text_area("Enter your message")
            st.button("Send")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
