import plotly.express as px
import pandas as pd
import streamlit as st

## Code for packaging type
# Packaging [W1501]
# Paper and cardboard packaging [W150101]
# Plastic packaging [W150102]
# Wooden packaging [W150103]
# Metallic packaging [W150104]
# Aluminium packaging [W15010401]
# Steel packaging [W15010402]
# Glass packaging [W150107]
# Other packaging [W150199]

# Wasting operator (wst_oper)
# Waste generated [GEN]
# Recovery [RCV]
# Recovery - energy recovery from packaging waste [RCV_E_PAC]
# Recovery - other [RCV_OTH]
# Recycling [RCY]
# Recycling in the Member State [RCY_NAT]
# Recycling in other Member States of the EU [RCY_EU_FOR]
# Recycling outside the EU [RCY_NEU]
# Repair [RPR]
# rating per country [RATING]

# Unit code
# RT = RATE
# T = TONNE
# KG_HAB = Kilograms per capita
# PC = Percentage

link="./data/env_waspac_linear.csv"
df=pd.read_csv(link)

def recyclage_per_country(data=df, country="PT", unit="T", select_operator = ["GEN"], type = df["waste"].unique()[0]):

    gen_waste_per_geo = pd.pivot_table(\
                     data=data[data["TIME_PERIOD"]==data["TIME_PERIOD"].max()],
                     index=["geo","waste", "wst_oper",'unit',],
                     values=["OBS_VALUE"],
                     aggfunc="mean",
                     dropna=False
                     ).reset_index()
    cols_op = ["geo","Waste type","Waste operator", "Unit", "Average"]
    gen_waste_per_geo.columns = cols_op

    #gen_waste_per_geo = gen_waste_per_geo[gen_waste_per_geo["Waste operator"].isin(gen_waste_per_geo["Waste operator"].unique())]
    # st.dataframe(gen_waste_per_geo[(gen_waste_per_geo['Waste operator'].isin(select_operator))\
    #  & (gen_waste_per_geo['geo'].isin([country, "EU27_2020"]))\
    #  & (gen_waste_per_geo['Waste type'] == type)\
    #  & (gen_waste_per_geo['Unit']==unit)])
    fig = px.bar(gen_waste_per_geo[(gen_waste_per_geo['Waste operator'].isin(select_operator))\
     & (gen_waste_per_geo['geo'].isin([country, "EU27_2020"]))\
     & (gen_waste_per_geo['Waste type'] == type)\
     & (gen_waste_per_geo['Unit']==unit)],
                   x="Waste operator",
                   y="Average",
                   #y_axis=range(0, 4000000),
                   #animation_frame="TIME_PERIOD",
                   #animation_group="OBS_VALUE",
                   color='geo',
                   labels={'Waste operation'},
                   width=800,
                   barmode="group")
    #fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig
