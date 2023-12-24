
import dash
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
from dash import dcc, html

dash.register_page(__name__, paths='/', name="Breast Cancer Data Analysis ")

breastcancer = pd.read_csv('./breastcancerdataset.csv')

# Remove 'Unnamed' columns if present
breastcancer = breastcancer.loc[:, ~breastcancer.columns.str.contains('^Unnamed')]

# Identify non-numeric columns and drop them (or convert them as needed)
non_numeric_columns = breastcancer.select_dtypes(exclude=[np.number]).columns
breastcancer_numeric = breastcancer.drop(non_numeric_columns, axis=1)

# Calculate the correlation matrix and round the values
corr_matrix = breastcancer_numeric.corr().round(3)

# Create a heatmap
fig_corr_matrix = ff.create_annotated_heatmap(
    z=corr_matrix.to_numpy(),
    x=list(corr_matrix.columns),
    y=list(corr_matrix.index),
    colorscale='Viridis',
    showscale=True
)

# Update layout for readability
fig_corr_matrix.update_layout(
    height=600,
    width=600,
    title_text='Correlation Matrix',
    xaxis={'side': 'bottom'}
)

# Create histograms for selected features
fig_hist_age = px.histogram(breastcancer, x='Age', nbins=20, title="Age Distribution")
fig_hist_tumor_size = px.histogram(breastcancer, x='Tumor Size', nbins=20, title="Tumor Size Distribution")
fig_hist_survival_months = px.histogram(breastcancer, x='Survival Months', nbins=20, title="Survival Months Distribution")

# page layout
layout = html.Div(children=[
    html.Div(children=[

    dcc.Graph(id='correlation-matrix', figure=fig_corr_matrix),

    html.H2("Data Distributions", style={'text-align': 'center'}),
    dcc.Graph(id='histogram-age', figure=fig_hist_age),
    dcc.Graph(id='histogram-tumor-size', figure=fig_hist_tumor_size),
    dcc.Graph(id='histogram-survival-months', figure=fig_hist_survival_months)
    ])
])