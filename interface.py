# Import libraries
import pandas as pd
import streamlit as st
# import seaborn as sn
# from matplotlib import pyplot as plt
# import plotly.express as px
# from sklearn.preprocessing import StandardScaler
# from sklearn.neighbors import NearestNeighbors
# from unidecode import unidecode
# from sklearn.preprocessing import MultiLabelBinarizer


#df = pd.read_csv("./data/rating_movies_audience_publisher")

st.markdown('<H1 style="color:#00cc00;text-align:center;" >Green app</H1>', unsafe_allow_html=True)

st.markdown('<style>.row-widget.stButton{display: flex;justify-content: center;}</style>', unsafe_allow_html=True)


nav_list = [
            "intro",
            ]

us_title = "About us"

with st.sidebar:
    selected = st.selectbox(
         '',
         options=nav_list)
    if st.button(us_title):
        selected = us_title

if selected==nav_list[0]:
    st.write("Test")

if selected==us_title:
    st.markdown(f'# {us_title}')
    us = [
    {"name":"Fabien Martinez",
     "img": "https://media-exp1.licdn.com/dms/image/C5603AQHJnh0UtSOiog/profile-displayphoto-shrink_200_200/0/1517442681233?e=1657756800&v=beta&t=LyfuwkU19EGf5Hyp5akMGx_rzIqGzo8bH1VreVcKq0k",
    "linkedin":"https://www.linkedin.com/in/fabien-martinez-a30561109/"},
    {"name":"François de la Bretèche",
    "img": "https://media-exp1.licdn.com/dms/image/C4D03AQG9QwJ6igbmKA/profile-displayphoto-shrink_800_800/0/1584797342559?e=1657756800&v=beta&t=hiwVl_fchl2uEhZph6uheK_59vq5QRJixzqiGkKTvoo",
    "linkedin":"https://www.linkedin.com/in/f-delabreteche/"},
    {"name":"Joana Alves",
    "img": "https://media-exp1.licdn.com/dms/image/C4D03AQFhUPgrR5wVUg/profile-displayphoto-shrink_800_800/0/1558610964713?e=1657756800&v=beta&t=zYzStxavELhinCITmuVNygzu3nH00jP3LLFKmv6hVkM",
    "linkedin":"https://www.linkedin.com/in/joana-pires-coelho/"
    },
    {"name":"João Almeida",
    "img": "https://raw.githubusercontent.com/FMrtnz/project_movie_recommand/main/img/joao2.png",
    "linkedin":"https://github.com/The-Ineffable-Alias"}
    ]

    st.markdown(
    "<style>.us-card{text-align:center; margin:.8rem 0}.us-card p{margin:.3rem 0}.us-card img{-webkit-filter: grayscale(100%);filter: grayscale(100%);border-radius:50%;width:150px;height:150px;padding:1rem;}</style>",
    unsafe_allow_html=True
    )
    col1, col2, col3, col4 = st.columns(4)
    cols = [col1, col2, col3, col4]
    for index in range(0,4):
        with cols[index]:
            one = us[index]
            st.markdown(
            f'<div class="us-card"><img src="{one["img"]}"><p>{one["name"]}</p><a href="{one["linkedin"]}">linkedin</a>',
            unsafe_allow_html=True
            )
