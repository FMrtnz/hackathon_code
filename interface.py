# Import libraries
import pandas as pd
import streamlit as st
from europe_map import create_a_map_europe
import plotly.express as px
from recyclage import recyclage_per_country
import numpy as np
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
df['wst_oper'].fillna("RATING", inplace=True)

st.markdown('<H1 style="color:#00cc00;text-align:center;" >Green app</H1>', unsafe_allow_html=True)

st.markdown('<style>.row-widget.stButton{display: flex;justify-content: center;}</style>', unsafe_allow_html=True)


nav_list = [
            "Europe map",
            "Waste vs recovery",
            "Different types of recovery",
            "Recycling per country vs Europe Union"
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
    # # Set a select menu
    # country_list = df["geo"].unique()
    # options = st.multiselect(
     # 'Select a country',
     # country_list,
     # country_list[0])
    ######################################################
    ######################################################
    # FRANCOIS

    link = "./data/env_waspac_linear.csv"
    df = pd.read_csv(link)
    # Importing Generated waste and Recovered waste data from 2019 only (excluding geo=EU27_2020 data)
    df_wst_rcv_19 = df[(df['TIME_PERIOD'] == 2019) & (df['wst_oper'].isin(['GEN','RCV']) & (df['geo'] != 'EU27_2020'))][['geo','wst_oper','unit','OBS_VALUE']].copy()

    # Droping a few rows that don't have values to be observed
    df_wst_rcv_19.dropna(axis=0, subset=['OBS_VALUE'], inplace=True)

    # Renaming GEN and RCV for the chart legend to be clearer
    df_wst_rcv_19['wst_oper'].replace('GEN','Generated',inplace=True)
    df_wst_rcv_19['wst_oper'].replace('RCV','Recovered',inplace=True)

    # Generating the dataframe for the bar plot
    df_chart = df_wst_rcv_19.groupby(['unit','geo','wst_oper']).sum()

    # Defining a dictionnary linking units codes with units names
    units_dict = {'kg per capita':'KG_HAB', 'tons':'T', 'percent':'PC'}

    # Dropdown menu to select the unit
    unit_choice = st.selectbox('Select units:', units_dict)

    # Generating the bar plot in the chosen unit
    plot = px.bar(df_chart.loc[units_dict[unit_choice]].reset_index(), x='geo', y='OBS_VALUE', color='wst_oper',barmode='group',labels={"GEN": "Generated", "RCV": "Recovered"})

    # Customizing bar plot before display
    plot.update_layout(xaxis_showgrid=False, yaxis_showgrid=False,paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',legend_title="Waste")
    plot.update_xaxes(title="Countries")
    plot.update_yaxes(title="Value (" + unit_choice + ")")

    # Displaying the bar plot
    st.plotly_chart(plot)
    ######################################################
    ######################################################

if selected==nav_list[2]:
    st.markdown(f'## {nav_list[2]}')
    # Set a select menu
    #country_list = df["geo"].unique()
    #options = st.multiselect(
     #'Select a country',
     #country_list,
     #country_list[0])
    ######################################################
    ######################################################
    # JOAO



    link = "./data/env_waspac_linear.csv"
#link = 'https://raw.githubusercontent.com/FMrtnz/hackathon_code/main/data/env_waspac_linear.csv'df = pd.read_csv(link)

# Importing Generated waste and Recovered waste data from 2019 only (excluding geo=EU27_2020 data)
    rcv_19 = df[(df['TIME_PERIOD'] == 2019) & (df['wst_oper'].isin(['RCV_OTH','RCY','RCV_E_PAC']) & (df['geo'] != 'EU27_2020'))][['geo','wst_oper','unit','OBS_VALUE']].copy()

# Droping a few rows that don't have values to be observed
    rcv_19.dropna(axis=0, subset=['OBS_VALUE'], inplace=True)

# Renaming GEN and RCV for the chart legend to be clearer
    rcv_19['wst_oper'].replace('RCY','Recycled',inplace=True)

    rcv_19['wst_oper'].replace('RCV_OTH','Recovery - other',inplace=True)

    rcv_19['wst_oper'].replace('RCV_E_PAC','Energy recovered from packaging waste',inplace=True)


#Generating the dataframe for the bar plot
    df_chart = rcv_19.groupby(['unit','geo','wst_oper']).sum()

#Defining a dictionnary linking units codes with units names
#units_dict = {'kg per capita':'KG_HAB', 'tons':'T', 'percent':'PC'}

#Dropdown menu to select the unit
#unit_choice = st.selectbox('Select units:', units_dict)

#Dropdown menu to select the country


    country_choice = st.multiselect('Select countries:',options=  df_chart.loc['KG_HAB'].reset_index().geo.unique(),default= ['PT', 'FR', 'DE','IT','ES'])


#Generating the bar plot in the chosen unit
    df_multiselect = df_chart.loc['KG_HAB'].reset_index()



    plot = px.bar(df_multiselect[df_multiselect['geo'].isin(country_choice)], x='geo', y='OBS_VALUE', color='wst_oper',barmode='group')

#Customizing bar plot before display
    plot.update_layout(xaxis_showgrid=False, yaxis_showgrid=False,paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',legend_title="Waste")
    plot.update_xaxes(title="Countries")
    plot.update_yaxes(title="KG PER CAPITA")

#Displaying the bar plot
    st.plotly_chart(plot)

    ######################################################
    ######################################################


if selected==nav_list[3]:
# Recycling in the Member State [RCY_NAT]
# Recycling in other Member States of the EU [RCY_EU_FOR]
# Recycling outside the EU [RCY_NEU]
# Repair [RPR]
    country_list = df["geo"].unique()
    col1,col2,col3 = st.columns(3)

    with col1:
        sel_country = st.selectbox(
         'Select a country',
         country_list)
        country_list = df["geo"].unique()

    with col2:
        unit_list = ["T", "RT", "KG_HAB"]
        unit_selected = st.selectbox(
         'Select unit',
         unit_list)

    with col3:
        type_list = df["waste"].unique()
        type_selected = st.selectbox(
         'Select type of packaging',
         type_list)


    if unit_selected!="RT":
        list_op = np.delete(df["wst_oper"].unique(), np.where(df["wst_oper"].unique() == "RATING"))
    else:
        list_op=["RATING"]

    sel_op = st.multiselect(
     'Select Operator',
     list_op,
     list_op)


    st.plotly_chart(recyclage_per_country(df,sel_country,unit_selected, sel_op, type_selected))

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
