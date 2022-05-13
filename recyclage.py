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
                     data=data[(data["geo"]==country)& \
                     data["TIME_PERIOD"]==data["TIME_PERIOD"].max() &\
                     (data["unit"]==unit)\
                     & (data['waste'] == type)
                     ],
                     index=["wst_oper"],
                     values=["OBS_VALUE"],
                     aggfunc="mean"
                     ).reset_index()

    gen_waste_total = pd.pivot_table(\
                     data=data[(data["geo"]=="eur28")& \
                     data["TIME_PERIOD"]==data["TIME_PERIOD"].max() &\
                     (data["unit"]==unit)\
                     & (data['waste'] == type)
                     ],
                     index=["wst_oper"],
                     values=["OBS_VALUE"],
                     aggfunc="mean"
                     ).reset_index()
    cols_op = ["Waste operator", "Average"]
    gen_waste_total.columns = cols_op
    gen_waste_total["geo"] = "Europe"
    gen_waste_per_geo.columns = cols_op
    gen_waste_per_geo["geo"] = country
    gen_waste_per_geo = gen_waste_per_geo[gen_waste_per_geo["Waste operator"].isin(gen_waste_total["Waste operator"].unique())]
    df_final = pd.concat([gen_waste_per_geo, gen_waste_total])
    fig = px.bar(df_final[df_final['Waste operator'].isin(select_operator)],
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
