import dash
from dash import Dash, html, dcc
import pandas as pd
from dash.dependencies import Input, Output, State
import numpy as np
import plotly
import plotly.graph_objects as go
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

px.defaults.template = "ggplot2"

external_css =  ["https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css",]
app = Dash(__name__, pages_folder='pages', use_pages=True, external_stylesheets=external_css)


app.layout = html.Div([
    html.Br(),
    html.P('Breast Cancer Dashboard App', className="text-dark text-center fw-bold fs-1"),
    html.Img(src='https://i.postimg.cc/YCkm38TB/breastcancer.jpg',
             style={'width': '100%', 'display': 'inline-block'}),
    html.Div(children=[
        dcc.Link(page['name'], href=page["relative_path"], className="btn btn-dark m-2 fs-5") \
        for page in dash.page_registry.values()]
    ),
    dash.page_container,
], className="col-8 mx-auto")


if __name__ == '__main__':
    app.run(debug=True)
