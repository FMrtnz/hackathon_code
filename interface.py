# Import libraries
import pandas as pd
import streamlit as st
from europe_map import create_a_map_europe

## Code for packaging type
# Packaging [W1501] # Paper and cardboard packaging [W150101] Plastic packaging [W150102] Wooden packaging [W150103] Metallic packaging [W150104] Aluminium packaging [W15010401] Steel packaging [W15010402] Glass packaging [W150107] Other packaging [W150199]

# Wasting operator (wst_oper) Waste generated [GEN] Recovery [RCV] Recovery - energy recovery from packaging waste [RCV_E_PAC] Recovery - other [RCV_OTH] Recycling [RCY] Recycling in the Member State [RCY_NAT] Recycling in other Member States of the EU [RCY_EU_FOR] Recycling outside the EU [RCY_NEU] Repair [RPR] rating per country [RATING]
# Unit code RT = RATE T = TONNE PC = Percentage KG_HAB = Kilograms per capita

# DATABASE Packaging waste by waste management operations
link="./data/env_waspac_linear.csv"
df1=pd.read_csv(link)
# Rating database
link2 = "./data/env_waspacr_linear.csv"
df_waspacr = pd.read_csv(link2)
# Combine TABLE
df=pd.concat([df1,df_waspacr])



st.markdown('<H1 style="color:#00cc00;text-align:center;" >Green app</H1>', unsafe_allow_html=True)

st.markdown('<style>.row-widget.stButton{display: flex;justify-content: center;}</style>', unsafe_allow_html=True)


nav_list = [
            "Europe map",
            "Waste vs recovery",
            "Different types of recovery"
            ]

us_title = "About us"

with st.sidebar:
    selected = st.selectbox(
         '',
         options=nav_list)
    if st.button(us_title):
        selected = us_title

if selected==nav_list[0]:
    st.markdown(f'## {nav_list[0]}')
    # select one value Waste generated [GEN] & Recovery [RCV]
    op = ["Waste generate","Recovery"]
    # 2 maps with 2 metrics T = TON & KG_HAB = Kilograms per capita
    sel_country = st.selectbox(
         'Display maps by :',
         options=op,
         key=[0, 1]
         )
    values=[
         {"sel": "GEN", "label": "Waste generate"},
         {"sel": "RCV", "label": "Recovery"},
    ]
    index = 0
    if sel_country == op[1]:
        index = 1
    st.write(f'{values[index]["label"]} (Tons)')
    st.plotly_chart(create_a_map_europe(values[index]["sel"], 'Tons'))
    st.write(f'{values[index]["label"]} (kg/hab)')
    st.plotly_chart(create_a_map_europe(values[index]["sel"], 'kg/hab', "KG_HAB"))

if selected==nav_list[1]:
    st.markdown(f'## {nav_list[1]}')
    # Set a select menu
    country_list = df["geo"].unique()
    options = st.multiselect(
     'What are your favorite colors',
     country_list,
     country_list[0])
    ######################################################
    ######################################################
    # FRANCOIS
    ######################################################
    ######################################################

if selected==nav_list[2]:
    st.markdown(f'## {nav_list[2]}')
    # Set a select menu
    country_list = df["geo"].unique()
    options = st.multiselect(
     'What are your favorite colors',
     country_list,
     country_list[0])
    ######################################################
    ######################################################
    # JOAO
    ######################################################
    ######################################################

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
