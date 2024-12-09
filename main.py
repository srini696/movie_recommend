import streamlit as st
import streamlit_option_menu
from streamlit_extras.stoggle import stoggle
from streamlit_option_menu import option_menu
from processing import preprocess
from processing.display import Main

# Setting the wide mode as default

import streamlit as st
import time

# Set up Streamlit page
st.set_page_config(
    page_title="Movie Hub",
    page_icon="🎥",
    layout="wide",
)

# Use session state to manage loading status
if "loading_complete" not in st.session_state:
    st.session_state.loading_complete = False

# Display the loading screen if not complete
if not st.session_state.loading_complete:
    # Add custom CSS for Netflix-like loading animation
    st.markdown(
        """
        <style>
        body {
            background-color: #141414;  /* Netflix Black */
        }
        .netflix-loading {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: #E50914;  /* Netflix Red */
            font-size: 24px;
            font-weight: bold;
            animation: pulse 1.5s infinite;
        }

        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    
   

# Use HTML and CSS to create a Netflix-style logo
    st.markdown(
    """
    <style>
    /* Center container to the middle of the page */
    html, body, [data-testid="stAppViewContainer"] {
        height: 100%;
        margin: 0;
    }
    
    /* Center content with flexbox */
    [data-testid="stAppViewContainer"] {
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: black; /* Optional: adds a black background */
    }
    .netflix-style {
        font-family: 'Arial Black', sans-serif;
        font-size: 60px;
        color: #e50914; /* Netflix red */
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        text-align: center;
        margin-top: 20px;
    }
    </style>
    <div class="netflix-style">MOVIE ARENA...</div>
    """,
    unsafe_allow_html=True
    )

    time.sleep(3)  # Simulated delay for loading
    st.session_state.loading_complete = True  # Set loading as complete
    st.experimental_rerun()  # Rerun to display the main content

# Main content page
else:
    # Netflix-like main content
    st.markdown(
        """
        <style>
        body {
            background-color: #141414;  /* Netflix Black */
            color: #FFFFFF;  /* Netflix White */
            font-family: 'Arial', sans-serif;
        }
        .header-title {
            color: #E50914;  /* Netflix Red */
            font-size: 36px;
            font-weight: bold;
        }
        .content {
            margin-top: 20px;
            font-size: 20px;
            color: #B3B3B3;  /* Netflix Light Gray */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Main page content
    st.markdown('<h1 class="header-title">🎥 Welcome to Movie Arena</h1>', unsafe_allow_html=True)
    st.markdown('<p class="content">Explore movies and get personalized recommendations!</p>', unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .page-title {
        color: white;  /* Set title color to black */
        font-size: 36px;  /* Adjust font size */
        font-weight: bold;  /* Make it bold */
        margin-bottom: 20px;  /* Add spacing below the title */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the page title
st.markdown('<h1 class="page-title">🎥 Movie Recommendation System</h1>', unsafe_allow_html=True)

displayed = []


if 'movie_number' not in st.session_state:
    st.session_state['movie_number'] = 0

if 'selected_movie_name' not in st.session_state:
    st.session_state['selected_movie_name'] = ""

if 'user_menu' not in st.session_state:
    st.session_state['user_menu'] = ""


def main():
    def initial_options():
        
        # To display menu

# Customizing the menu with styles
        st.session_state.user_menu = option_menu(
        menu_title="🎥 Movie Hub - Explore Movies!",  # Title for the menu
        options=[
        "🎬 Recommend me a similar movie", 
        "🎥 Describe me a movie", 
        "📜 Check all Movies"
        ],  # Menu options
        icons=["play-circle", "info-circle", "list"],  # FontAwesome icons
        menu_icon="film",  # Main menu icon
        default_index=0,  # Default selected index
        orientation="horizontal",  # Horizontal layout
        styles={
        "container": {
            "padding": "0px",
            "background-color": "#E50914",  # Light beige for a movie-like feel
        },
        "icon": {
            "color": "#292929",  # Icon color (orange-red)
            "font-size": "20px",  # Icon size
        },
        "nav-link": {
            "font-size": "18px",  # Text size
            "margin": "0px",
            "padding": "5px",
            "color": "#333",  # Text color
            "text-align": "center",
            "background-color": "transparent",
            "border-radius": "5px",
        },
        "nav-link-selected": {
            "background-color": "#FC5A50",  # Selected link background color
            "color": "white",  # Text color for the selected item
        },
        },
        )
        

# Display content based on selected menu
        if st.session_state.user_menu == "🎬 Recommend me a similar movie":
            st.title("✨ Recommend a Movie")
            st.markdown("Here you can get movie recommendations based on your preferences!")
            recommend_display()

        elif st.session_state.user_menu == "🎥 Describe me a movie":
            st.title("📖 Movie Details")
            st.markdown("Enter the name of a movie to see its details!")
            display_movie_details()

        elif st.session_state.user_menu == "📜 Check all Movies":
            st.title("📜 Browse Movies")
            st.markdown("Explore all the movies in our database!")
            paging_movies()

    def recommend_display():

        selected_movie_name = st.selectbox(
            'Choose a Movie from below...', new_df['title'].values
        )

        rec_button = st.button('Recommend')
        if rec_button:
            st.session_state.selected_movie_name = selected_movie_name
            recommendation_tags(new_df, selected_movie_name, r'Files/similarity_tags_tags.pkl',"are")
            recommendation_tags(new_df, selected_movie_name, r'Files/similarity_tags_genres.pkl',"on the basis of genres are")
            recommendation_tags(new_df, selected_movie_name,
                                r'Files/similarity_tags_tprduction_comp.pkl',"from the same production company are")
            recommendation_tags(new_df, selected_movie_name, r'Files/similarity_tags_keywords.pkl',"on the basis of keywords are")
            recommendation_tags(new_df, selected_movie_name, r'Files/similarity_tags_tcast.pkl',"on the basis of cast are")

    def recommendation_tags(new_df, selected_movie_name, pickle_file_path,str):

        movies, posters = preprocess.recommend(new_df, selected_movie_name, pickle_file_path)
        st.subheader(f'Best Recommendations {str}...')

        rec_movies = []
        rec_posters = []
        cnt = 0
        # Adding only 5 uniques recommendations
        for i, j in enumerate(movies):
            if cnt == 5:
                break
            if j not in displayed:
                rec_movies.append(j)
                rec_posters.append(posters[i])
                displayed.append(j)
                cnt += 1

        # Columns to display informations of movies i.e. movie title and movie poster
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(rec_movies[0])
            st.image(rec_posters[0])
        with col2:
            st.text(rec_movies[1])
            st.image(rec_posters[1])
        with col3:
            st.text(rec_movies[2])
            st.image(rec_posters[2])
        with col4:
            st.text(rec_movies[3])
            st.image(rec_posters[3])
        with col5:
            st.text(rec_movies[4])
            st.image(rec_posters[4])

    def display_movie_details():

        selected_movie_name = st.session_state.selected_movie_name
        # movie_id = movies[movies['title'] == selected_movie_name]['movie_id']
        info = preprocess.get_details(selected_movie_name)

        with st.container():
            image_col, text_col = st.columns((1, 2))
            with image_col:
                st.text('\n')
                st.image(info[0])

            with text_col:
                st.text('\n')
                st.text('\n')
                st.title(selected_movie_name)
                st.text('\n')
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.text("Rating")
                    st.write(info[8])
                with col2:
                    st.text("No. of ratings")
                    st.write(info[9])
                with col3:
                    st.text("Runtime")
                    st.write(info[6])

                st.text('\n')
                st.write("Overview")
                st.write(info[3], wrapText=False)
                st.text('\n')
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.text("Release Date")
                    st.text(info[4])
                with col2:
                    st.text("Budget")
                    st.text(info[1])
                with col3:
                    st.text("Revenue")
                    st.text(info[5])

                st.text('\n')
                col1, col2, col3 = st.columns(3)
                with col1:
                    str = ""
                    st.text("Genres")
                    for i in info[2]:
                        str = str + i + " . "
                    st.write(str)

                with col2:
                    str = ""
                    st.text("Available in")
                    for i in info[13]:
                        str = str + i + " . "
                    st.write(str)
                with col3:
                    st.text("Directed by")
                    st.text(info[12][0])
                st.text('\n')

        # Displaying information of casts.
        st.header('Cast')
        cnt = 0
        urls = []
        bio = []
        for i in info[14]:
            if cnt == 5:
                break
            url, biography= preprocess.fetch_person_details(i)
            urls.append(url)
            bio.append(biography)
            cnt += 1

        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.image(urls[0])
            # Toggle button to show information of cast.
            stoggle(
                "Show More",
                bio[0],
            )
        with col2:
            st.image(urls[1])
            stoggle(
                "Show More",
                bio[1],
            )
        with col3:
            st.image(urls[2])
            stoggle(
                "Show More",
                bio[2],
            )
        with col4:
            st.image(urls[3])
            stoggle(
                "Show More",
                bio[3],
            )
        with col5:
            st.image(urls[4])
            stoggle(
                "Show More",
                bio[4],
            )

    def paging_movies():
        # To create pages functionality using session state.
        max_pages = movies.shape[0] / 10
        max_pages = int(max_pages) - 1

        col1, col2, col3 = st.columns([1, 9, 1])

        with col1:
            st.text("Previous page")
            prev_btn = st.button("Prev")
            if prev_btn:
                if st.session_state['movie_number'] >= 10:
                    st.session_state['movie_number'] -= 10

        with col2:
            new_page_number = st.slider("Jump to page number", 0, max_pages, st.session_state['movie_number'] // 10)
            st.session_state['movie_number'] = new_page_number * 10

        with col3:
            st.text("Next page")
            next_btn = st.button("Next")
            if next_btn:
                if st.session_state['movie_number'] + 10 < len(movies):
                    st.session_state['movie_number'] += 10

        display_all_movies(st.session_state['movie_number'])

    def display_all_movies(start):

        i = start
        with st.container():
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                id = movies.iloc[i]['movie_id']
                link = preprocess.fetch_posters(id)
                st.image(link, caption=movies['title'][i])
                i = i + 1

            with col2:
                id = movies.iloc[i]['movie_id']
                link = preprocess.fetch_posters(id)
                st.image(link, caption=movies['title'][i])
                i = i + 1

            with col3:
                id = movies.iloc[i]['movie_id']
                link = preprocess.fetch_posters(id)
                st.image(link, caption=movies['title'][i])
                i = i + 1

            with col4:
                id = movies.iloc[i]['movie_id']
                link = preprocess.fetch_posters(id)
                st.image(link, caption=movies['title'][i])
                i = i + 1

            with col5:
                id = movies.iloc[i]['movie_id']
                link = preprocess.fetch_posters(id)
                st.image(link, caption=movies['title'][i])
                i = i + 1

        with st.container():
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                id = movies.iloc[i]['movie_id']
                link = preprocess.fetch_posters(id)
                st.image(link, caption=movies['title'][i])
                i = i + 1

            with col2:
                id = movies.iloc[i]['movie_id']
                link = preprocess.fetch_posters(id)
                st.image(link, caption=movies['title'][i])
                i = i + 1

            with col3:
                id = movies.iloc[i]['movie_id']
                link = preprocess.fetch_posters(id)
                st.image(link, caption=movies['title'][i])
                i = i + 1

            with col4:
                id = movies.iloc[i]['movie_id']
                link = preprocess.fetch_posters(id)
                st.image(link, caption=movies['title'][i])
                i = i + 1

            with col5:
                id = movies.iloc[i]['movie_id']
                link = preprocess.fetch_posters(id)
                st.image(link, caption=movies['title'][i])
                i = i + 1

        st.session_state['page_number'] = i

    with Main() as bot:
        bot.main_()
        new_df, movies, movies2 = bot.getter()
        initial_options()


if __name__ == '__main__':
    main()
