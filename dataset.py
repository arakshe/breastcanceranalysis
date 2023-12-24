import pandas as pd
import dash
from dash import Dash, html, dash_table, dcc
import plotly.graph_objects as go

dash.register_page(__name__, path= '/dataset', name = "Dataset ")


#load dataset
breastcancer = pd.read_csv("./breastcancerdataset.csv")

layout = html.Div(children=[
    html.Br(), \
    dash_table.DataTable(data=breastcancer.to_dict('records'),
                         page_size=20,
                         style_cell={"background-color": "light-grey", "border":"solid 1px white", "color": "black", "font-size": "11px", "text-align": "left" },
                         style_header={"background-color":"dodger-blue", "font-weight": "bold", "color": "white", "padding": "10px", "font-size": "18px"},
                         ),
])
