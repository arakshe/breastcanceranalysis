import dash
from dash import html

dash.register_page(__name__, paths='/', name="Introduction :)")

# page layout
layout = html.Div(children=[
    html.Div(children=[
        html.H2("Breast Cancer Dataset Overview"),
        "This breast cancer dataset features the following columns: ",
        html.Br(),
        "Using this dashboard, you can explore potential risk factors of breast cancer",
        html.Br(),
        "Sending love <3 "
    ]),
    html.Div(children=[
        html.Br(),
        html.H2("Data Variables"),
        html.B("Dead or Alive"), "0 = No, 1 = Yes",
        html.Br(),
        html.B("pclass: "), "Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)",
    ])
], className="bg-light p-4 m-2")
