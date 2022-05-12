import pandas as pd
import json
import plotly.express as px

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

def create_a_map_europe(select_operator = "GEN", label="Waste generate (tons)", unit="T"):

    f = open(file="./data/europe.geo.json",mode='rb')
    contents = f.read()
    data = json.loads(contents)

    # I set an id to connect trought the value wb_a2
    for x in data["features"]:
        x['id'] = x["properties"]["wb_a2"]

    # CREATE A PIVOT TABLE gpe by country and type waste operator generate in last year in tonnes
    gen_waste_per_geo = pd.pivot_table(\
                     data=df[(df["unit"]==unit)&(df["TIME_PERIOD"]==df["TIME_PERIOD"].max()) & (df['wst_oper'] == select_operator)],
                     index=["geo"],
                     values=["OBS_VALUE"]
                     ).reset_index()

    # I connect the country trought the value wb_a2
    gen_waste_per_geo.columns = ["wb_a2", "OBS_VALUE"]

    value_max = int(gen_waste_per_geo["OBS_VALUE"].quantile(.9))

    fig = px.choropleth_mapbox(gen_waste_per_geo, geojson=data, locations='wb_a2',
                               color='OBS_VALUE',
                               color_continuous_scale="Viridis",
                               range_color=(0, value_max),
                               mapbox_style="carto-positron",
                               zoom=2, center = {"lat": 55, "lon": 0},
                               opacity=0.5,
                               labels={'OBS_VALUE':f'{label}'}
                              )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig
